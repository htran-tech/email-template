# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Tubi CRM email template system for Braze. Modular content blocks composed via Liquid templating into campaign HTML emails. No build step — blocks are pasted directly into Braze as Content Blocks.

## Architecture

**Blocks** (`blocks/*.html`) are self-contained Liquid + HTML table components. Campaigns include them via `{{content_blocks.${block_name}}}` and configure them with `{% assign %}` variables before each include. Every block:
- Declares defaults with `{% unless var %}{% assign var = default %}{% endunless %}`
- Conditionally renders (outputs nothing if required params missing)
- Auto-builds UTM params from campaign/canvas name
- Nulls all variables at the end to prevent cross-block bleed

**CSS** lives in `css-global.html`, included once in `<head>`. Mobile-first (600px base), desktop at `@media (min-width: 600px)` (800px container). Dark mode via `@media (prefers-color-scheme: dark)` and `[data-ogsc]`.

**Documentation:** `blocks/BLOCKS-API.md` has complete variable reference. `docs/BLOCKS.md` has architecture overview.

## Campaign Template (Braze-compatible)

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "...xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
  <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="format-detection" content="date=no" />
  <meta name="format-detection" content="address=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="x-apple-disable-message-reformatting" />
  <title>Campaign Title</title>
  <!--[if gte mso 9]><style type="text/css" media="all">sup{font-size:100%!important;}</style><![endif]-->
{{content_blocks.${css_global}}}
</head>
<body class="body" style="padding:0!important;margin:0 auto!important;display:block!important;min-width:100%!important;width:100%!important;background-color:#ffffff;-webkit-text-size-adjust:none;">
  <center>
    <table class="main-tb" width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
      <tr>
        <td align="center" valign="top">
          <table class="m-hide" style="mso-hide:all;" width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr><td style="font-size:0;line-height:0;">&nbsp;</td></tr>
            <tr><td style="font-size:0;line-height:0;">&#847;&zwnj;&nbsp;(repeated 150+ times)</td></tr>
          </table>
          <table role="presentation" class="email-container" cellpadding="0" cellspacing="0" border="0" width="600" bgcolor="#000000" style="max-width:600px;background-color:#000000;">
            <tr><td>
              {% assign tubi = "https://tubitv.com/home" %}
              {% assign utm = "?utm_source=braze&utm_medium=crm_email&utm_campaign=" | append: ... %}
              ... block includes ...
            </td></tr>
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
```

## Critical Constraints (Braze Preheader Compatibility)

These rules prevent Braze from breaking the email when its preheader feature is active:

1. **No `{% %}` Liquid tags in `<head>`** — only `{{output}}` tags. Liquid logic in head causes Braze to send as `text/plain`.
2. **No `{% %}` between `</head>` and `<body>`** — causes Braze to strip `class` and `style` from `<body>` tag, breaking the `u + .body` Gmail hack.
3. **XHTML doctype + xmlns required** — simple `<!doctype html>` causes Braze to destroy `<head>` entirely.
4. **No `{% if %}` inside HTML tag attributes in content blocks** — causes Braze to send as plain text. Pre-compute conditional values as variables before the HTML.
5. **No `width: Npx; height: Npx;` in style on `<img>` inside `<a>`** — triggers Gmail image zoom overlay instead of following the link. Use HTML `width`/`height` attributes only.

## Block Reference (quick)

| Block | Required params | Purpose |
|-------|----------------|---------|
| `css_global` | none | Global styles, in `<head>` only |
| `hero_single_title` | `hero_poster_url` | Hero with poster, logo, background |
| `single_cta` | `cta_label`, `cta_url` | Single button |
| `double_cta` | all four cta/cta2 label+url | Two buttons side-by-side |
| `headline_body` | `headline_copy` or `body_copy` | Text section |
| `image_only` | `image_url` | Full-width image |
| `image_device` | `image_url` | Device-conditional image |
| `poster_grid` | items (manual or `grid_result`) | Poster grid (1l/2l/2v/3v layouts) |
| `poster_list` | items (manual or `grid_result`) | Horizontal poster+text list |
| `behavioral_cards` | none (all have defaults) | Continue Watching / My List cards |
| `footer` | none (auto-detects locale) | Footer with badges, social, legal |

## Testing

No automated tests. Workflow is:
1. Edit block HTML locally
2. Paste into Braze Content Block editor
3. Send test email from Braze campaign
4. Verify in Gmail (desktop + mobile), Apple Mail, Outlook

Check rendered output by requesting `.eml` file via "Show Original" in Gmail, then inspect with Python's `email` module.

## Git

Only `blocks/`, `docs/`, and `Assets/` are tracked (see `.gitignore`). The `sample/` directory is gitignored — campaign files are reference/test only.
