# Email Template Blocks Reference

## Architecture

All blocks are Braze Content Blocks written in Liquid + HTML tables. They follow consistent patterns:
- Defaults via `{% unless %}` at the top
- Conditional rendering (block outputs nothing if required params missing)
- Auto-built UTM parameters from campaign/canvas name
- Variable cleanup (null assignment) at the end to prevent cross-block bleed
- Mobile-first responsive design with desktop `@media (min-width: 600px)` breakpoints
- Dark mode support via `@media (prefers-color-scheme: dark)` and `[data-ogsc]`

## Campaign Template Structure

Campaigns must use this wrapper for Braze preheader compatibility:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "...">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <!--[if gte mso 9]><xml>...</xml><![endif]-->
  <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="format-detection" content="date=no" />
  <meta name="format-detection" content="address=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="x-apple-disable-message-reformatting" />
  <title>Campaign Title</title>
  <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
{{content_blocks.${css_global}}}
</head>
<body class="body" style="padding:0 !important; margin:0 auto !important; display:block !important; min-width:100% !important; width:100% !important; background:#ffffff; -webkit-text-size-adjust:none;">
  <center>
    <table class="main-tb" width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#ffffff">
      <tr>
        <td align="center" valign="top">
          <table class="m-hide" style="mso-hide: all;" width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr><td style="font-size:0pt;line-height:0pt;">&nbsp;</td></tr>
            <tr><td style="font-size:0pt;line-height:0pt;">&#847;&zwnj;&nbsp;...repeated 150+ times...</td></tr>
          </table>
          <table role="presentation" class="email-container" cellpadding="0" cellspacing="0" border="0" width="600" bgcolor="#000000" style="max-width:600px; background-color:#000000;">
            <tr><td>
              ... content blocks here ...
            </td></tr>
          </table>
        </td>
      </tr>
    </table>
  </center>
</body>
</html>
```

**Rules:**
- No `{% %}` Liquid logic tags in `<head>` (only `{{output}}` tags)
- XHTML doctype + xmlns required for Braze to preserve `<head>`
- Preheader whitespace hack inside `.m-hide` table in `<body>`
- `{% assign %}` variables go inside `<body>`

## Content Block Constraints

- No `{% if %}` conditionals inside HTML tag attributes within content blocks (causes Braze preheader to send as `text/plain`)
- Pre-compute conditional values as variables before the HTML output
- No `style="width: Npx; height: Npx;"` on `<img>` inside `<a>` tags (triggers Gmail image zoom instead of link click)

---

## css-global.html

Global CSS block included in `<head>`. Contains all typography, button styles, layout utilities, dark mode overrides, and responsive breakpoints.

**Key classes:**
| Class | Purpose |
|-------|---------|
| `.t-headline` | 40px bold uppercase, white |
| `.t-body` | 24px normal, white |
| `.t-genre` | 16px bold uppercase, white |
| `.t-cta` | 24px bold, no-decoration |
| `.t-footer` | 13px normal, muted |
| `.cta-primary` | Yellow bg (#ffff13), black text, 200px radius |
| `.cta-secondary` | Transparent bg, white border, white text |
| `.cta-secondary-brand` | Transparent bg, yellow border, yellow text |
| `.email-container` | 600px mobile, 800px desktop |
| `.dm-bg-dark` | Dark mode background override |
| `.img-mobile` / `.img-desktop` | Show/hide based on viewport |

**Responsive breakpoint:** `@media screen and (min-width: 600px)` — container expands to 800px, fonts resize, poster/hero dimensions change.

**Liquid variables used:**
- `{{email_outer_bg | default: "transparent"}}` — `.email-wrapper` background
- `{{email_inner_bg | default: "transparent"}}` — `.email-container` background

---

## single-cta.html

Single full-width CTA button.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `cta_label` | (required) | Button text |
| `cta_url` | (required) | Click destination |
| `cta_style` | "primary" | "primary" / "secondary" / "secondary-brand" |
| `cta_width` | "full" | "full" (560px) / "auto" / pixel value |
| `cta_height` | 60 | Button height in px |
| `cta_radius` | 200 | Border radius in px |
| `cta_align` | "center" | "left" / "center" / "right" |
| `cta_padding_top` | 12 | Top padding in px |
| `cta_padding_bottom` | 12 | Bottom padding in px |
| `cta_clicktracking` | "on" | "on" / "off" |
| `utm_params` | auto | UTM string, or "false" to disable |

**Only renders if both `cta_label` and `cta_url` are set.**

---

## double-cta.html

Two side-by-side CTA buttons.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `cta_label` | (required) | Button 1 text |
| `cta_url` | (required) | Button 1 URL |
| `cta_style` | "primary" | Button 1 style |
| `cta2_label` | (required) | Button 2 text |
| `cta2_url` | (required) | Button 2 URL |
| `cta2_style` | "secondary" | Button 2 style |
| `dcta_gap` | 20 | Gap between buttons in px |
| `dcta_btn_width` | 270 | Each button width in px |
| `dcta_height` | 60 | Button height |
| `dcta_radius` | 200 | Border radius |

**Only renders if ALL four (cta_label, cta_url, cta2_label, cta2_url) are set.**

---

## headline-body.html

Headline text with optional body copy.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `headline_copy` | (optional) | Headline text |
| `headline_url` | (optional) | Makes headline a link |
| `body_copy` | (optional) | Body text below headline |
| `hb_align` | "center" | Text alignment |
| `hb_text_color` | "#ffffff" | Base text color |
| `hb_headline_color` | inherits | Override headline color |
| `hb_body_color` | inherits | Override body color |
| `hb_headline_transform` | "uppercase" | CSS text-transform value |
| `hb_headline_size` | (inherits) | Custom px size |
| `hb_body_size` | (inherits) | Custom px size |
| `hb_padding_top` | 42 | Top padding |
| `hb_padding_bottom` | 12 | Bottom padding |
| `hb_gap` | 8 | Gap between headline and body |

**Only renders if `headline_copy` or `body_copy` is set.**

---

## hero-single-title.html

Hero section with background image, logo, poster, and optional banner.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `hero_poster_url` | (required) | Poster image URL |
| `hero_variant` | "1" | Background variant (1, 2a, 2b, 3, 4) |
| `hero_orientation` | "portrait" | "portrait" (355x507) / "landscape" (560x315) |
| `hero_bg_url` | auto per variant | Background image (auto-assigned if not set) |
| `hero_border` | auto | "true" for variants 3/4, "false" otherwise |
| `hero_poster_link` | (optional) | Click-through URL for poster |
| `hero_title` | "Watch on Tubi" | Alt text for poster image |
| `hero_banner_text` | (optional) | Status bar text (e.g. "Picked For You") |
| `hero_logo_url` | Tubi logo | Logo image |
| `hero_logo_link` | tubitv.com/home | Logo click destination |

**Only renders if `hero_poster_url` is set.**

**Sizing:** Portrait = 355x507 mobile, 473x676 desktop. Landscape = 560x315 mobile, 747x420 desktop.

---

## image-only.html

Single full-width image with optional link.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `image_url` | (required) | Image source URL |
| `image_link` | (optional) | Click-through URL |
| `image_alt` | "Tubi" | Alt text |
| `image_width` | 600 | Image width |
| `image_border_radius` | 0 | Corner rounding in px |
| `image_margin_top` | 0 | Top margin |
| `image_margin_bottom` | 24 | Bottom margin |
| `image_margin_left` | 0 | Left margin |
| `image_margin_right` | 0 | Right margin |
| `image_clicktracking` | "on" | "on" / "off" |

**Only renders if `image_url` is set.**

---

## image-device.html

Conditional image rendering based on device type (app installed vs web).

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `image_url` | (required) | Desktop/web image |
| `image_mobile_url` | (optional) | Mobile-specific image |
| `image_link` | (optional) | Desktop click-through |
| `image_mobile_link` | inherits | Mobile click-through |
| `has_mobile` | (optional) | If "true", renders nothing (user has app) |
| `open_on_desktop` | (optional) | "true" = desktop only, "false" = mobile only, unset = auto-detect |

**Three rendering modes:** Desktop-only, mobile-only, or auto-detect (both rendered, CSS toggles visibility).

---

## poster-grid.html

Flexible poster grid with multiple layout options.

**Layout types:**
- `1l` — 1 landscape poster per row (560px wide)
- `2l` — 2 landscape posters per row (274px each)
- `2v` — 2 vertical posters per row (274px each)
- `3v` — 3 vertical posters per row (178px each)

**Four rendering modes:**

1. **API Mode** — Set `grid_result` to API response object:
```liquid
{% assign grid_result = result %}
{% assign grid_container_index = 0 %}
{% assign grid_utm_params = utm %}
{{content_blocks.${poster_grid}}}
```

2. **Mixed Rows** — Set `grid_rows` for custom layout sequence:
```liquid
{% assign grid_rows = "1l,3v,2l" %}
{% assign grid_item_1_img = "..." %}
{% assign grid_item_1_url = "..." %}
...
{{content_blocks.${poster_grid}}}
```

3. **Uniform Layout** — Set `grid_layout` for repeated row type:
```liquid
{% assign grid_layout = "3v" %}
{% assign grid_items_limit = 6 %}
{{content_blocks.${poster_grid}}}
```

4. **Auto** — Neither set; uses item count to auto-build layout.

**Key Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `grid_layout` | "3v" | Uniform row type |
| `grid_rows` | (optional) | Comma-separated row sequence (e.g. "1l,3v,2l") |
| `grid_items_limit` | 18 | Max items to render |
| `grid_result` | (optional) | API response object for auto-population |
| `grid_container_index` | 0 | Which container from API response |
| `grid_headline` | "" | Section heading |
| `grid_headline_url` | "" | Heading link |
| `grid_cta_label` | "" | Bottom CTA text |
| `grid_cta_url` | "" | Bottom CTA link |
| `grid_cta_style` | "secondary" | CTA style |
| `grid_show_metadata` | "false" | Show genre/title |
| `grid_show_genre` | inherits | Show genre text |
| `grid_show_title` | inherits | Show title text |
| `grid_meta_align` | "left" | Metadata alignment |
| `grid_meta_position` | "below" | "above" / "below" poster |
| `grid_cta_watch` | "false" | Auto-add Watch Now per item |
| `grid_cta_mylist` | "false" | Auto-add My List per item |
| `grid_text_color` | "#ffffff" | Text color |
| `grid_utm_params` | auto | UTM or "false" |

**Per-item variables** (N = 1-18):
- `grid_item_N_img` — Vertical poster image
- `grid_item_N_landscape_img` — Landscape image (used for 1l/2l rows)
- `grid_item_N_url` — Click-through
- `grid_item_N_genre` — Genre text
- `grid_item_N_subhead` — Title/description
- `grid_item_N_cta_label` / `_cta_url` — Per-item CTA

---

## poster-list.html

Horizontal list with poster + metadata side by side.

**Layout:** Each row is one item rendered as poster image on one side, text metadata on the other.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `grid_layout` | "l" | "l" = poster left, "r" = poster right |
| `grid_rows` | (optional) | Alternating layout (e.g. "l,r,l,r") |
| `grid_result` | (optional) | API response for auto-population |
| `grid_container_index` | 0 | API container index |
| `grid_headline` | "" | Section heading |
| `grid_cta_label` | "" | Bottom CTA |
| `grid_cta_url` | "" | Bottom CTA link |
| `grid_show_metadata` | "false" | Show genre/title |
| `grid_cta_watch` | "false" | Per-item Watch Now |
| `grid_cta_mylist` | "false" | Per-item My List |
| `grid_text_color` | "#ffffff" | Text color |

**Per-item variables** (N = 1-18):
- `grid_item_N_img` — Poster image
- `grid_item_N_url` — Click-through
- `grid_item_N_headline` — Bold title
- `grid_item_N_subhead` — Description
- `grid_item_N_genre` — Genre tags
- `grid_item_N_cta_label` / `_cta_url` — CTA button
- `grid_item_N_cta2_label` / `_cta2_url` — Second CTA

---

## behavioral-cards.html

Promotional cards for Continue Watching and My List.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `bcard_show_cw` | "true" | Show Continue Watching card |
| `bcard_show_ml` | "true" | Show My List card |
| `bcard_cw_heading` | "Continue Watching" | CW card heading |
| `bcard_cw_body` | "Something you started is almost gone." | CW card body |
| `bcard_cw_cta_label` | "Watch Now" | CW button text |
| `bcard_cw_url` | continue_watching URL | CW click-through |
| `bcard_cw_bg` | "#45009D" | CW card background |
| `bcard_ml_heading` | "My List" | ML card heading |
| `bcard_ml_body` | "Don't let your great taste go to waste." | ML card body |
| `bcard_ml_cta_label` | "Watch Now" | ML button text |
| `bcard_ml_url` | queue URL | ML click-through |
| `bcard_ml_bg` | "#8C00E5" | ML card background |

**API auto-toggle:** Set `bcard_result_cw` / `bcard_result_ml` to API count results to auto-hide cards with no data.

**Renders:** 2 cards side-by-side (268px each) when both visible, or 1 full-width card. Hides entirely if both off.

---

## footer.html

Locale-aware footer with logo, app badges, social icons, unsubscribe, and legal.

**Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `footer_lang` | auto-detected | "en" / "es" / "pt" / "fr" |
| `footer_country` | auto-detected | "US" / "CA" / "AU" / "GB" / "NZ" / "MX" / "BR" |
| `footer_show_badges` | "true" | Show app store badges |
| `footer_show_social` | "true" | Show social icons |
| `footer_badge_stores` | "appstore,gplay" | Which badges to show |
| `footer_social_icons` | "tiktok,instagram,x,facebook" | Which icons to show |

**Country-aware:** App store and social URLs adjust per country. Language auto-detected from Braze `${language}` or derived from country.

**Slot-based:** Add custom badges/icons by extending the comma-separated lists and setting corresponding `footer_social_{name}_url` / `_icon` / `_alt` variables.

---

## UTM Pattern (shared across all blocks)

All blocks with links use this UTM logic:

```liquid
{% if utm_params == "false" %}
  {% assign _utm = "" %}
{% elsif utm_params != blank %}
  {% assign _utm = utm_params %}
{% else %}
  {% if campaign.name != blank %}
    {% assign _utm_name = campaign.name | url_encode %}
  {% elsif canvas.name != blank %}
    {% assign _utm_name = canvas.name | url_encode %}
  {% else %}
    {% assign _utm_name = "braze_email" %}
  {% endif %}
  {% assign _utm = "?utm_source=braze&utm_medium=crm_email&utm_campaign=" | append: _utm_name %}
{% endif %}
```

- Set `utm_params = "false"` to disable UTM entirely
- Set `utm_params = "?custom=value"` to use custom UTM
- Leave unset for auto-detection from campaign/canvas name
