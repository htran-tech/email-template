# Blocks API Reference

Variable reference for all Tubi CRM email template content blocks.

---

## email_header

Campaign HTML wrapper (DOCTYPE through opening `<td>`). Includes XHTML doctype, Office XML, meta tags, css_global, preheader whitespace hack, and email-container opening. No parameters — just include it as the first line of every campaign.

```liquid
{{content_blocks.${email_header}}}
```

**Provides:** White outer background (#ffffff), black inner background (#000000), 600px mobile / 800px desktop container, preheader compatibility, Gmail `u + .body` hack.

---

## email_footer

Closing HTML tags for the campaign wrapper. Include as the last line of every campaign (after the `footer` block).

```liquid
{{content_blocks.${email_footer}}}
```

---

## Campaign Quick Start

```liquid
{{content_blocks.${email_header}}}

{% assign tubi = "https://tubitv.com/home" %}
{% capture _utm_campaign %}{{campaign.${name}}}{% endcapture %}
{% assign utm = "?utm_source=braze&utm_medium=crm_email&utm_campaign=" | append: _utm_campaign %}

{% assign hero_poster_url = "POSTER_IMAGE_URL" %}
{% assign hero_orientation = "portrait" %}
{% assign hero_poster_link = "DESTINATION_URL" %}
{% assign hero_title = "Watch on Tubi" %}
{% assign hero_variant = "1" %}
{% assign hero_logo_link = tubi %}
{{content_blocks.${hero_single_title}}}

{% assign headline_copy = "Your Headline" %}
{% assign body_copy = "Your body text here." %}
{{content_blocks.${headline_body}}}

{% assign cta_label = "Watch Now" %}
{% assign cta_url = "DESTINATION_URL" | append: utm %}
{{content_blocks.${single_cta}}}

{% assign footer_lang = "en" %}
{% assign footer_country = "US" %}
{{content_blocks.${footer}}}

{{content_blocks.${email_footer}}}
```

---

## behavioral-cards

Two side-by-side cards for "Continue Watching" and "My List".
Each card can be toggled on/off independently.
If only one is visible, it renders full-width centered. If both are off, nothing renders.

### Toggles
| Variable | Values | Default |
|----------|--------|---------|
| `bcard_show_cw` | `"true"` \| `"false"` | `"true"` |
| `bcard_show_ml` | `"true"` \| `"false"` | `"true"` |

### Continue Watching
| Variable | Description | Default |
|----------|-------------|---------|
| `bcard_cw_heading` | Heading text | `"Continue Watching"` |
| `bcard_cw_body` | Body copy | `"Something you started is almost gone."` |
| `bcard_cw_cta_label` | CTA button text | `"Watch Now"` |
| `bcard_cw_url` | Click-through URL | `"https://tubitv.com/category/continue_watching"` |
| `bcard_cw_bg` | Card background color | `"#45009D"` |
| `bcard_cw_cta_bg` | CTA button background | `"rgba(255,255,255,0.2)"` |
| `bcard_cw_cta_color` | CTA button text color | `"#ffffff"` |

### My List
| Variable | Description | Default |
|----------|-------------|---------|
| `bcard_ml_heading` | Heading text | `"My List"` |
| `bcard_ml_body` | Body copy | `"Don't let your great taste go to waste."` |
| `bcard_ml_cta_label` | CTA button text | `"Watch Now"` |
| `bcard_ml_url` | Click-through URL | `"https://tubitv.com/category/queue"` |
| `bcard_ml_bg` | Card background color | `"#8C00E5"` |
| `bcard_ml_cta_bg` | CTA button background | `"rgba(255,255,255,0.2)"` |
| `bcard_ml_cta_color` | CTA button text color | `"#ffffff"` |

### API Auto-Toggle (optional)
| Variable | Description |
|----------|-------------|
| `bcard_result_cw` | API trigger data for CW (if `.count > 0`, show CW card) |
| `bcard_result_ml` | API trigger data for ML (if `.count > 0`, show ML card) |

### Layout
| Variable | Description | Default |
|----------|-------------|---------|
| `content_bg_color` | Outer background | from `email_inner_bg` |
| `bcard_padding_top` | Top padding in px | `12` |
| `bcard_padding_bottom` | Bottom padding in px | `12` |

---

## double-cta

Two side-by-side CTA buttons with individually configurable colors.
Nothing renders if any of `cta_label`, `cta_url`, `cta2_label`, `cta2_url` is blank.

### Button 1
| Variable | Description | Default |
|----------|-------------|---------|
| `cta_label` | Button text | (required) |
| `cta_url` | Button link | (required) |
| `cta_style` | `"primary"` \| `"secondary"` \| `"secondary-brand"` | `"primary"` |
| `cta_bg_color` | Override button bg | from preset |
| `cta_text_color` | Override button text color | from preset |
| `cta_border_color` | Override button border (`"none"` = no border) | from preset |

### Button 2
| Variable | Description | Default |
|----------|-------------|---------|
| `cta2_label` | Button text | (required) |
| `cta2_url` | Button link | (required) |
| `cta2_style` | `"primary"` \| `"secondary"` \| `"secondary-brand"` | `"secondary"` |
| `cta2_bg_color` | Override button bg | from preset |
| `cta2_text_color` | Override button text color | from preset |
| `cta2_border_color` | Override button border (`"none"` = no border) | from preset |

### Tracking & Layout
| Variable | Description | Default |
|----------|-------------|---------|
| `cta_clicktracking` | `"on"` \| `"off"` (applies to both) | `"on"` |
| `content_bg_color` | Content area background | `"#000000"` |
| `dcta_gap` | Gap between buttons in px | `20` |
| `dcta_padding_top` | Top padding in px | `12` |
| `dcta_padding_bottom` | Bottom padding in px | `12` |
| `dcta_align` | `"left"` \| `"center"` \| `"right"` | `"center"` |
| `dcta_radius` | Shared border radius in px | `200` |
| `dcta_height` | Shared button height in px | `60` |
| `dcta_btn_width` | Per-button width in px | `270` |

---

## footer

Full footer card with logo, app store badges, social icons, unsubscribe, and legal.
Every variable can be set by the caller. Unset variables receive locale-aware defaults.

### Locale
| Variable | Description | Default |
|----------|-------------|---------|
| `footer_lang` | `"en"` \| `"es"` \| `"pt"` \| `"fr"` | auto from Braze `${language}` or derived from country |
| `footer_country` | `"US"` \| `"CA"` \| `"AU"` \| `"GB"` \| `"NZ"` \| `"MX"` \| `"BR"` | auto from Braze `${country}`, fallback `"US"` |

### Toggles
| Variable | Values | Default |
|----------|--------|---------|
| `footer_show_badges` | `"true"` \| `"false"` | `"true"` |
| `footer_show_social` | `"true"` \| `"false"` | `"true"` |

### Assets
| Variable | Description |
|----------|-------------|
| `footer_logo_url` | Tubi logo image |
| `footer_logo_link` | Logo click-through |

### App Store Badges (slot-based)
| Variable | Description | Default |
|----------|-------------|---------|
| `footer_badge_stores` | Comma-separated slot list | `"appstore,gplay"` |
| `footer_badge_{slot}_img` | Badge image URL | built-in |
| `footer_badge_{slot}_link` | Badge click-through (country-aware) | built-in |
| `footer_badge_{slot}_alt` | Badge alt text | built-in |

### Social Icons (slot-based)
| Variable | Description | Default |
|----------|-------------|---------|
| `footer_social_heading` | Heading text | `"Let's be social"` (locale-aware) |
| `footer_social_icons` | Comma-separated slot list | `"tiktok,instagram,x,facebook"` |
| `footer_social_{slot}_url` | Icon link | built-in |
| `footer_social_{slot}_icon` | Icon image URL | built-in |
| `footer_social_{slot}_alt` | Icon alt text | built-in |

### Legal / Copy
| Variable | Description |
|----------|-------------|
| `footer_unsub_text` | Unsubscribe blurb (locale-aware) |
| `footer_unsub_link_text` | Unsubscribe link label (locale-aware) |
| `footer_unsubscribe` | Unsubscribe URL (Braze default) |
| `footer_sent_from` | Sender line (locale-aware) |
| `footer_address` | Company address |
| `footer_copyright` | Copyright label |
| `footer_rights` | Rights text (locale-aware) |

### Background
| Variable | Description | Default |
|----------|-------------|---------|
| `footer_content_bg` | Card background | `"rgba(45,45,45,0.85)"` |
| `footer_content_bg_fallback` | Solid hex fallback for Outlook | `"#262626"` |

---

## headline-body

Standalone headline with optional body copy.
Nothing renders if neither `headline_copy` nor `body_copy` is set.

### Content
| Variable | Description |
|----------|-------------|
| `headline_copy` | Headline text |
| `headline_url` | Optional link wrapping the headline |
| `body_copy` | Body text |

### Font Sizes
| Variable | Description | Default |
|----------|-------------|---------|
| `hb_headline_size` | Headline font-size in px | inherits `.t-headline` |
| `hb_body_size` | Body font-size in px | inherits `.t-body` |

### Colors
| Variable | Description | Default |
|----------|-------------|---------|
| `content_bg_color` | Content area background | `"#000000"` |
| `hb_text_color` | Text color for both | `"#ffffff"` |
| `hb_headline_color` | Headline-specific color | same as `hb_text_color` |
| `hb_body_color` | Body-specific color | same as `hb_text_color` |

### Tracking & Layout
| Variable | Description | Default |
|----------|-------------|---------|
| `hb_clicktracking` | `"on"` \| `"off"` | `"on"` |
| `hb_align` | `"left"` \| `"center"` \| `"right"` | `"center"` |
| `hb_padding_top` | Top padding in px | `42` |
| `hb_padding_bottom` | Bottom padding in px | `12` |
| `hb_padding_side` | Side padding in px | `20` |
| `hb_gap` | Gap between headline and body in px | `8` |
| `hb_headline_transform` | `"uppercase"` \| `"none"` \| `"capitalize"` | `"uppercase"` |

---

## hero-single-title

Hero section with background image, Tubi logo, and title poster card.

### Required
| Variable | Description |
|----------|-------------|
| `hero_poster_url` | Title poster image URL (block won't render without it) |

### Visual Variant
| Variable | Description | Default |
|----------|-------------|---------|
| `hero_variant` | Background treatment: `"1"` \| `"2a"` \| `"2b"` \| `"3"` \| `"4"` | `"1"` |
| `hero_border` | Yellow border around poster: `"true"` \| `"false"` | `"false"` (auto `"true"` for variants 3 & 4) |
| `hero_orientation` | Poster shape: `"portrait"` \| `"landscape"` | `"portrait"` |

### Background
| Variable | Description | Default |
|----------|-------------|---------|
| `hero_bg_url` | Background image URL | Braze production purple gradient |

### Logo
| Variable | Description | Default |
|----------|-------------|---------|
| `hero_logo_url` | Tubi logo image | Braze production asset |
| `hero_logo_link` | Logo click-through | `https://tubitv.com/home` |

### Poster
| Variable | Description | Default |
|----------|-------------|---------|
| `hero_poster_link` | Click-through URL for the poster | (optional) |
| `hero_title` | Title text for alt attribute | `"Watch on Tubi"` |

### Banner Status Bar
| Variable | Description |
|----------|-------------|
| `hero_banner_text` | Status text e.g. "Picked For You", "Leaving Soon" (shows only when set) |

---

## image-device

Conditional image: renders desktop or mobile image based on user attributes.
Renders nothing if the user has the mobile app (`has_mobile = true`).

### Scenarios
- `has_mobile = true` → nothing rendered
- `has_mobile = false/unset` + `open_on_desktop = true` → desktop image only
- `has_mobile = false/unset` + `open_on_desktop = false` → mobile image only
- `has_mobile = false/unset` + `open_on_desktop` unset → auto CSS detection

### Required
| Variable | Description |
|----------|-------------|
| `image_url` | Desktop image source URL |
| `image_mobile_url` | Mobile image source URL |
| `has_mobile` | Truthy if user has the mobile app |
| `open_on_desktop` | `true`: desktop only; `false`: mobile only; unset: auto-detect |

### Optional
| Variable | Description | Default |
|----------|-------------|---------|
| `image_link` | Click-through URL for desktop image | |
| `image_mobile_link` | Click-through URL for mobile image | `image_link` |
| `image_alt` | Alt text for desktop image | `"Tubi"` |
| `image_mobile_alt` | Alt text for mobile image | `image_alt` |
| `image_width` | HTML width attribute for Outlook | `600` |
| `image_border_radius` | Border radius in px | `0` |
| `image_margin_top` | Top spacing in px | `0` |
| `image_margin_bottom` | Bottom spacing in px | `0` |
| `image_margin_left` | Left spacing in px | `0` |
| `image_margin_right` | Right spacing in px | `0` |
| `content_bg_color` | Content area background | `"transparent"` |

---

## image-only

Standalone image. Nothing renders if `image_url` is blank.
Full-bleed by default (all margins 0).

### Required
| Variable | Description |
|----------|-------------|
| `image_url` | Image source URL |

### Optional
| Variable | Description | Default |
|----------|-------------|---------|
| `image_link` | Click-through URL | |
| `image_alt` | Alt text | `"Tubi"` |
| `image_width` | HTML width attribute for Outlook | `600` |
| `image_border_radius` | Border radius in px | `0` |
| `image_margin_top` | Top spacing in px | `0` |
| `image_margin_bottom` | Bottom spacing in px | `24` |
| `image_margin_left` | Left spacing in px | `0` |
| `image_margin_right` | Right spacing in px | `0` |
| `image_clicktracking` | `"on"` \| `"off"` | `"on"` |
| `content_bg_color` | Content area background | `"#000000"` |

---

## poster-grid

Flexible grid block supporting layouts: 1L, 2L, 2V, 3V in uniform or mixed-row configurations.

### Four Modes
1. **API mode**: Set `grid_result = result` (auto-resolves items + smart layout)
2. **Mixed rows**: Set `grid_rows="1l,3v,2l"` + sequential items
3. **Uniform rows**: Set `grid_layout="2v"` + sequential items (auto-fills rows)
4. **Auto**: Just set items, no `grid_rows`/`grid_layout` — uses count%3 smart layout

### Layout Types (items consumed per row)
| Type | Description | Mobile | Desktop |
|------|-------------|--------|---------|
| `1l` | 1 landscape | 560x315 | 720x405 |
| `2l` | 2 landscape | 274x154 | 352x198 |
| `2v` | 2 vertical | 274x392 | 352x504 |
| `3v` | 3 vertical | 178x256 | 229x329 |

Max 18 items | Max 6 rows

### Grid Configuration
| Variable | Description | Default |
|----------|-------------|---------|
| `grid_headline` | Optional section headline above the grid | |
| `grid_headline_url` | Optional link on the headline | |
| `grid_body` | Optional body copy below headline | |
| `grid_cta_label` | Section CTA button label (below grid) | |
| `grid_cta_url` | Section CTA button URL | |
| `grid_cta_style` | `"primary"` \| `"secondary"` \| `"secondary-brand"` | `"primary"` |
| `grid_rows` | Comma-separated row layouts e.g. `"1l,3v,2l"` | |
| `grid_layout` | Uniform layout for all rows | `"3v"` |
| `grid_cta_watch` | Auto-apply "Watch Now" button to every item | `"false"` |
| `grid_cta_watch_label` | Override watch button text | `"Watch Now"` |
| `grid_cta_mylist` | Auto-apply "+ My List" button to every item | `"false"` |
| `grid_cta_mylist_label` | Override mylist button text | `"+ My List"` |
| `grid_items_limit` | Max items to render (hard max: 18) | `18` |
| `grid_show_metadata` | Show both genre + title | `"false"` |
| `grid_show_genre` | Show genre independently | follows `grid_show_metadata` |
| `grid_show_title` | Show title independently | follows `grid_show_metadata` |
| `grid_meta_align` | Metadata text alignment: `"left"` \| `"center"` | `"left"` |
| `grid_meta_position` | Genre position: `"below"` \| `"above"` | `"below"` |
| `content_bg_color` | Content area background | `"#000000"` |
| `grid_text_color` | Text color for headline/metadata | `"#ffffff"` |

### Content Items (up to 18)
| Variable | Description |
|----------|-------------|
| `grid_item_N_img` | Poster image URL (vertical/portrait) |
| `grid_item_N_landscape_img` | Landscape image URL (optional; falls back to `_img`) |
| `grid_item_N_url` | Click-through URL |
| `grid_item_N_subhead` | Subhead/title text |
| `grid_item_N_genre` | Genre tags (use `•` for separators) |
| `grid_item_N_cta_label` | Per-item CTA button text |
| `grid_item_N_cta_url` | Per-item CTA button link |

### API Mode
| Variable | Description | Default |
|----------|-------------|---------|
| `grid_result` | Raw API result object | |
| `grid_container_index` | Which container to render | `0` |
| `grid_api_items` | Pass items array directly (legacy/override) | |
| `grid_utm_params` | UTM string (`"false"` to disable) | auto-built |

---

## poster-grid-frame

**Full drop-in replacement for `poster-grid`** — every layout (`1l`/`2l`/`2v`/`3v`), every data mode (API `grid_result`,
mixed `grid_rows`, uniform `grid_layout`, auto mod-3), landscape image swap, metadata, per-item CTAs, Watch/My List, and
section headline/body/CTA — **plus an optional decorative frame overlay on every poster**. With `grid_frame = "none"`
(the default) it behaves exactly like `poster-grid`. See TCAMPOPTIM-214.

> **Two-block install (Braze 51,200-char cap):** this module is split into two Content Blocks. Register **both** in
> Braze: **`poster_grid_frame`** (the one campaigns call) and its companion **`poster_grid_frame_render`** (internal —
> `poster_grid_frame` includes it automatically; never call it directly). Campaigns are unchanged: still just
> `{{content_blocks.${poster_grid_frame}}}`. Both files are generated together — see
> `blocks/poster-grid-frame.html` (setup) and `blocks/poster-grid-frame-render.html` (render); keep them in sync.

The block **auto-selects the frame asset by layout**: `2v`/`3v` → portrait frame; `1l` (full width) → **big** horizontal
frame; `2l` (narrow) → **small** horizontal frame. The user just picks a number `1–9` (or a URL, or `"none"`) and the
right orientation/resolution is chosen automatically.

**Framed cell keeps the frame's aspect** (portrait 0.707, horizontal 1.416) so the frame art is never distorted; the
poster sits in the transparent window via `object-fit:cover`. Unframed cells keep poster-grid's native 16:9 for `1l`/`2l`.

**Graceful fallback (required):** the poster is always a real, linked `<img>`. If the frame can't render — Gmail's
inconsistent `background-size`, Outlook without VML, or a failed asset load — the poster still shows on `content_bg_color`
and stays clickable. Frame compositing is reliable in Apple Mail (macOS/iOS), best-effort in Gmail, VML in Outlook.

### Frame selection (the only thing this adds over poster-grid)
| Variable | Description | Default |
|----------|-------------|---------|
| `grid_frame` | Frame for **every** poster: a number `"1"`–`"9"`, a custom URL, or `"none"` | `"none"` |
| `grid_item_N_frame` | Per-slot override (N = 1–18): number `"1"`–`"9"`, custom URL, or `"none"`; falls back to `grid_frame` | `grid_frame` |
| `grid_frame_url` | Legacy alias — a single URL for all posters; used as the fallback for `grid_frame` if set | — |

Resolution per slot: `grid_item_N_frame` → else `grid_frame` → interpret (URL if it contains `://`, else look up the
numbered frame in the set matching that cell's layout, else `none` = plain poster). A custom URL is used as-is for any
layout, so if you override with a URL make sure it matches the cell's orientation.

### All other variables
Identical to **[poster-grid](#poster-grid)** — `grid_result`, `grid_container_index`, `grid_rows`, `grid_layout`,
`grid_items_limit`, `grid_item_N_img/_url/_subhead/_genre/_landscape_img/_cta_label/_cta_url`, `grid_headline*`,
`grid_body`, `grid_cta_*`, `grid_item_cta_style`, `grid_cta_watch(_label)`, `grid_cta_mylist(_label)`,
`grid_show_metadata/_genre/_title`, `grid_meta_align`, `grid_meta_position`, `content_bg_color`, `grid_text_color`,
`grid_dot_color`. See the poster-grid section for full descriptions.

### Built-in frame sets (frames `"1"`–`"9"`, 3 orientations each)
Baked into the block; referenced by number. To swap artwork, edit the `_fs_v_raw` / `_fs_lg_raw` / `_fs_sm_raw` captures
at the top of `blocks/poster-grid-frame.html` — campaigns keep using the same `"1"`–`"9"` numbers. Braze Media Library ids:

| # | Portrait (`2v`/`3v`) | Big horizontal (`1l`) | Small horizontal (`2l`) |
|---|---|---|---|
| 1 | 6a7a1694d56c4300889e5195 | 6a7ca2fb8f565e008885cad5 | 6a7ca25a6cd3dd008812d3ee |
| 2 | 6a7a169437ff3000887540c4 | 6a7ca2f9d7bb3c00867c76e4 | 6a7ca25b2a461a008a43aa5c |
| 3 | 6a7a1694fd692d0086858299 | 6a7ca2f9f39e1d00864333f4 | 6a7ca25bd198a500880d31be |
| 4 | 6a7a16940d9cf700864bc663 | 6a7ca2fbb4ea7c0088d26607 | 6a7ca25a6f113d00a3b2ff66 |
| 5 | 6a7a16944e59b30088a1c352 | 6a7ca2fb38cd9400882ae0d9 | 6a7ca25af9e6010088c5a275 |
| 6 | 6a7a1693b852f20088cff348 | 6a7ca2f9c21e7a0088dad72d | 6a7ca25a210ea200886e7588 |
| 7 | 6a7a1693843bed008a92d9d7 | 6a7ca2f97365e10088005868 | 6a7ca25a424cc300883aaee8 |
| 8 | 6a7a16938d1a020086933037 | 6a7ca2f8bfa9f0008ab1a5c9 | 6a7ca259d445d80086d465ae |
| 9 | 6a7a1693d7904f00863ce8e5 | 6a7ca2f8d9a169008404ecce | 6a7ca2596f113d0088b30527 |

Note: `1l` uses the **big** (~1.3–2 MB) frame since it's full-width; `2l` uses the **small** (~180–280 KB) frame. Stacking
many `1l` framed rows in one email adds weight — prefer it for a single hero row.

### Examples
```liquid
{% assign grid_result = result %}
{% assign grid_show_metadata = "true" %}

{% comment %} all posters framed with set 3; layout auto-picks portrait vs horizontal {% endcomment %}
{% assign grid_frame = "3" %}
{{content_blocks.${poster_grid_frame}}}

{% comment %} mixed layout: 1 landscape hero + a row of 3 portraits, all framed {% endcomment %}
{% assign grid_rows = "1l,3v" %}
{% assign grid_frame = "1" %}
{{content_blocks.${poster_grid_frame}}}

{% comment %} per-slot frame numbers + a custom override {% endcomment %}
{% assign grid_item_1_frame = "1" %}
{% assign grid_item_2_frame = "5" %}
{% assign grid_item_3_frame = "https://braze-images.com/.../custom.png" %}
{{content_blocks.${poster_grid_frame}}}
```

---

## poster-list

List-style block: each row shows one item as a horizontal pair (poster + metadata side by side).

### Layout Types (1 item per row)
| Type | Description |
|------|-------------|
| `l` | Poster LEFT, metadata RIGHT |
| `r` | Poster RIGHT, metadata LEFT |

Poster: 274x392 mobile, 352x504 desktop | Text: 262px mobile, 336px desktop | Gap: 24px mobile, 32px desktop

Max 18 items | Max 18 rows

### Grid Configuration
| Variable | Description | Default |
|----------|-------------|---------|
| `grid_rows` | Comma-separated row layouts e.g. `"l,r,l,r"` | |
| `grid_layout` | Uniform layout for all rows: `"l"` \| `"r"` | `"l"` |
| `grid_headline` | Optional headline text above list | |
| `grid_headline_url` | Optional headline link | |
| `grid_body` | Optional body copy below headline | |
| `grid_cta_label` | Optional CTA button label below list | |
| `grid_cta_url` | Optional CTA button link | |
| `grid_cta_style` | `"primary"` \| `"secondary"` \| `"secondary-brand"` | `"primary"` |
| `grid_show_metadata` | Show both genre + title | `"false"` |
| `grid_show_genre` | Show genre independently | follows `grid_show_metadata` |
| `grid_show_title` | Show title independently | follows `grid_show_metadata` |
| `grid_text_color` | Text color | `"#ffffff"` |
| `content_bg_color` | Content area background | `"transparent"` |

### Global Per-Item CTAs
| Variable | Description | Default |
|----------|-------------|---------|
| `grid_cta_watch` | Show "Watch Now" on all items | `"false"` |
| `grid_cta_watch_label` | Override button text | `"Watch Now"` |
| `grid_cta_mylist` | Show "+ My List" on all items | `"false"` |
| `grid_cta_mylist_label` | Override button text | `"+ My List"` |
| `grid_cta_mylist_url` | Optional custom URL for all watchlist buttons | |

### Content Items (up to 18)
| Variable | Description |
|----------|-------------|
| `grid_item_N_img` | Poster image URL |
| `grid_item_N_url` | Click-through URL |
| `grid_item_N_headline` | Headline text (bold uppercase) |
| `grid_item_N_subhead` | Subhead text |
| `grid_item_N_genre` | Genre tags (use `•` for separators) |
| `grid_item_N_cta_label` | Per-item CTA button text |
| `grid_item_N_cta_url` | Per-item CTA button link |
| `grid_item_N_cta2_label` | Second per-item CTA button text |
| `grid_item_N_cta2_url` | Second per-item CTA button link |

### API Mode
| Variable | Description | Default |
|----------|-------------|---------|
| `grid_result` | Raw API result object | |
| `grid_container_index` | Which container to render | `0` |
| `grid_api_items` | Pass items array directly (legacy/override) | |
| `grid_utm_params` | UTM string (`"false"` to disable) | auto-built |

---

## single-cta

Standalone single CTA button. Nothing renders if `cta_label` or `cta_url` is blank.

### Content
| Variable | Description |
|----------|-------------|
| `cta_label` | Button text (required) |
| `cta_url` | Button link (required) |

### Style
| Variable | Description | Default |
|----------|-------------|---------|
| `cta_style` | `"primary"` \| `"secondary"` \| `"secondary-brand"` | `"primary"` |
| `cta_bg_color` | Button background | from preset |
| `cta_text_color` | Button text color | from preset |
| `cta_border_color` | Button border color (`"none"` = no border) | from preset |
| `cta_width` | `"full"` \| `"auto"` \| px value | `"full"` (560px) |

### Tracking & Layout
| Variable | Description | Default |
|----------|-------------|---------|
| `cta_clicktracking` | `"on"` \| `"off"` | `"on"` |
| `content_bg_color` | Content area background | `"#000000"` |
| `cta_padding_top` | Top padding in px | `12` |
| `cta_padding_bottom` | Bottom padding in px | `12` |
| `cta_align` | `"left"` \| `"center"` \| `"right"` | `"center"` |
| `cta_radius` | Border radius in px | `200` |
| `cta_height` | Button height in px | `60` |
