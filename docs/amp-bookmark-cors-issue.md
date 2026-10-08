# AMP Bookmark Error Fallback — Backend CORS Issue

## What works
- User taps "+ My List" → POST to `/api/v1/amp/bookmark` → server returns **200** → `submit-success` fires → icon toggles to bookmarked state ✓

## What doesn't work
- When the bookmark fails (invalid token, empty userId, etc.) → server returns **401** → `submit-error` should fire → "Try Again" link should replace the button → **nothing happens**

## Root cause
Gmail's AMP runtime has different CORS requirements for success vs error responses:

| Response | Required headers | Current state |
|----------|-----------------|---------------|
| **200 (success)** | `Access-Control-Allow-Origin` | ✓ Works — Gmail is lenient |
| **4xx (error)** | `Access-Control-Allow-Origin` + `AMP-Access-Control-Allow-Source-Origin` + `Access-Control-Expose-Headers` | ❌ Missing last two headers |

The endpoint currently returns on **all** responses:
```
access-control-allow-origin: https://mail.google.com
```

But for error responses (4xx/5xx), Gmail additionally requires:
```
AMP-Access-Control-Allow-Source-Origin: https://mail.google.com
Access-Control-Expose-Headers: AMP-Access-Control-Allow-Source-Origin
```

Without these, Gmail silently discards the error response. The AMP runtime never receives it, so neither `submit-error` nor `AMP.setState` fires — the button just does nothing.

## What needs to change (backend)
Add two headers to **all non-2xx responses** from `/api/v1/amp/bookmark`:

```
AMP-Access-Control-Allow-Source-Origin: https://mail.google.com
Access-Control-Expose-Headers: AMP-Access-Control-Allow-Source-Origin
```

Ideally add them to 200 responses too for correctness, but it's only strictly required on errors.

## Reference
- [AMP CORS Security Docs](https://amp.dev/documentation/guides-and-tutorials/learn/amp-caches-and-cors/amp-cors-requests/)
- The `AMP-Access-Control-Allow-Source-Origin` value should match the sender's origin — for Gmail this is always `https://mail.google.com`

## What we've built (email side — ready to go once backend is fixed)
- On error → `AMP.setState({errors:{i1: true}})` fires
- Form hides via `<div [hidden]="errors.i1">`
- "Try Again" `<a href>` link appears in the same position, linking to the content page
- All email-side code is complete and tested — just waiting on the backend header fix
