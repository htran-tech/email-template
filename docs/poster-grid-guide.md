# Poster Grid: Old vs New Workflow

> **TL;DR** — We replaced 3 separate grid blocks with **1 universal block** (`poster_grid`).
> Same results, fewer moving parts, and new layout options that weren't possible before.

---

## Before & After at a Glance

| | **OLD** (3+ blocks) | **NEW** (1 block) |
|---|---|---|
| **Grid blocks to learn** | `manual_title_grid` `ML_multi_container` (+ numbered variants) | `poster_grid` |
| **API data fetch** | `API_Connected_Content` content block | Inline `connected_content` call (same API, same `result`) |
| **Hand-picked titles** | Separate block, 4 variables per title | Same block, 2 variables per title |
| **API / algorithm content** | 2-block combo (API fetch block + ML renderer block) | 1 step: point `poster_grid` at the API data |
| **Switching layout size** | Pick a different block | Change one setting: `grid_layout` |
| **Mix poster sizes in one section** | Not possible | Set `grid_rows` (e.g. `"1l,3v,2l"`) |
| **Genre & title labels** | Not available | Toggle on/off, left or center, above or below |
| **"Watch Now" button per poster** | Not available | Set per-item CTA label + link |
| **Max posters** | 9 (manual) / varies (API) | 18 items, 6 rows |

> **Note on the API call:** The new workflow still fetches recommendations from the same ML API.
> The difference is that the `connected_content` call is now written directly in the campaign
> (not wrapped in a separate `API_Connected_Content` block). The result is saved to `result`
> and `poster_grid` reads from `result.containers[N].items` — same data, fewer layers.

---

## Layout Options

The new block supports 4 poster sizes. Pick the one that fits your section:

```
  3v — 3 Vertical (default)       2v — 2 Vertical
  ┌──────┐ ┌──────┐ ┌──────┐     ┌───────────┐ ┌───────────┐
  │      │ │      │ │      │     │           │ │           │
  │      │ │      │ │      │     │           │ │           │
  │      │ │      │ │      │     │           │ │           │
  └──────┘ └──────┘ └──────┘     │           │ │           │
                                  └───────────┘ └───────────┘

  1l — 1 Landscape (full width)   2l — 2 Landscape
  ┌──────────────────────────┐    ┌────────────┐ ┌────────────┐
  │                          │    │            │ │            │
  │                          │    └────────────┘ └────────────┘
  └──────────────────────────┘
```

You can mix these in a single section. For example, `grid_rows = "1l,3v,3v"` gives you one big landscape poster on top followed by two rows of 3 vertical posters.

---

## Real Campaign Comparison

Here's what changed between an actual old campaign and the new Kids UK campaign.

### OLD: Campaign 1 (Reese Witherspoon theme)

```
 ┌─────────────────────────────────────────┐
 │  Image Only block                       │  ← refresh_image_only
 ├─────────────────────────────────────────┤
 │  Manual Title Grid                      │  ← refresh_manual_title_grid
 │  9 titles, 36 variables                 │     (title_1_img, title_1_img_landscape,
 │  (Legally Blonde, Sweet Home Alabama…)  │      title_1_link, title_1  × 9 titles)
 ├─────────────────────────────────────────┤
 │  API Fetch                              │  ← API_Connected_Content (content block)
 │  (fetches 2000s_comedy + romance)       │     wraps the connected_content call
 ├─────────────────────────────────────────┤
 │  ML Container 1: "2000s Comedy"         │  ← refresh_ML_multi_container_1
 │  headline, subhead, CTA, 8 variables    │     renders grid from API data
 ├─────────────────────────────────────────┤
 │  ML Container 2: "Romance"              │  ← refresh_ML_multi_container_2
 │  headline, subhead, CTA, 8 variables    │     renders grid from API data
 ├─────────────────────────────────────────┤
 │  Footer                                 │  ← refresh_footer
 └─────────────────────────────────────────┘

 Content blocks used:  5 (3 different grid-related types)
 Grid variables:  ~52
```

### OLD: Campaign 2 (Nostalgia theme)

```
 ┌─────────────────────────────────────────┐
 │  Image Only block                       │  ← refresh_image_only
 ├─────────────────────────────────────────┤
 │  API Fetch                              │  ← API_Connected_Content (content block)
 │  (fetches cartoon_nostalgia, 10 items)  │     wraps the connected_content call
 ├─────────────────────────────────────────┤
 │  ML Container: "Cartoon Nostalgia"      │  ← refresh_ML_multi_container
 │  headline, CTA, 8 variables             │     renders grid from API data
 ├─────────────────────────────────────────┤
 │  Footer                                 │  ← refresh_footer
 └─────────────────────────────────────────┘

 Content blocks used:  3 (2 different grid-related types)
 Grid variables:  ~11
```

### NEW: Kids UK Campaign

```
 ┌─────────────────────────────────────────┐
 │  Hero                                   │  ← hero_single_title (×2)
 ├─────────────────────────────────────────┤
 │  Image Only                             │  ← image_only (×2)
 ├─────────────────────────────────────────┤
 │  API Fetch (inline connected_content)   │  ← same API, written directly
 │  (fetches 5 containers at once)         │     in campaign — no wrapper block
 ├─────────────────────────────────────────┤
 │  "Cartoon Nostalgia"  — 3v + genre      │  ← headline_body
 │  ┌──────┐ ┌──────┐ ┌──────┐            │  ← poster_grid  (API, 5 vars)
 │  │      │ │      │ │      │ + genre     │  ← single_cta
 │  └──────┘ └──────┘ └──────┘            │
 ├─────────────────────────────────────────┤
 │  "Leaving Soon"  — 3v + genre left      │  ← headline_body
 │  ┌──────┐ ┌──────┐ ┌──────┐            │  ← poster_grid  (API, 5 vars)
 │  │      │ │      │ │      │ + genre     │  ← single_cta
 │  └──────┘ └──────┘ └──────┘            │
 ├─────────────────────────────────────────┤
 │  "Epic Treasure Hunts" — 2v + buttons   │  ← headline_body
 │  ┌───────────┐ ┌───────────┐           │  ← poster_grid  (API, 9 vars)
 │  │           │ │           │ + genre    │  ← double_cta
 │  │ Watch Now │ │ Watch Now │           │
 │  └───────────┘ └───────────┘           │
 ├─────────────────────────────────────────┤
 │  "Kids Shows"  — 1l + genre above       │  ← headline_body
 │  ┌──────────────────────────┐           │  ← poster_grid  (API, 6 vars)
 │  │     GENRE • GENRE        │           │  ← single_cta
 │  │                          │           │
 │  └──────────────────────────┘           │
 ├─────────────────────────────────────────┤
 │  "Kid Classics"  — 3v, posters only     │  ← headline_body
 │  ┌──────┐ ┌──────┐ ┌──────┐            │  ← poster_grid  (API, 4 vars)
 │  │      │ │      │ │      │            │  ← single_cta
 │  └──────┘ └──────┘ └──────┘            │
 ├─────────────────────────────────────────┤
 │  "Coming Soon"  — 2l manual (×2)        │  ← headline_body
 │  ┌────────────┐ ┌────────────┐         │  ← poster_grid  (manual, 6 vars)
 │  └────────────┘ └────────────┘         │  ← poster_grid  (manual, 6 vars)
 │  ┌────────────┐ ┌────────────┐         │  ← single_cta
 │  └────────────┘ └────────────┘         │
 ├─────────────────────────────────────────┤
 │  Footer                                 │  ← footer
 └─────────────────────────────────────────┘

 Poster grid block used:  7 times (all the same block)
 Grid variables per section:  4–9
```

### The Takeaway

| | Campaign 1 (old) | Campaign 2 (old) | Kids UK (new) |
|---|---|---|---|
| **Grid block types** | 3 different | 2 different | **1 (poster_grid)** |
| **Grid block calls** | 4 | 2 | **7** |
| **Layout variety** | Fixed (one size) | Fixed (one size) | **4 sizes + mixed rows** |
| **Metadata under posters** | No | No | **Yes (toggleable)** |
| **Per-poster buttons** | No | No | **Yes** |

More sections, more variety, one block to learn.

---

## What You Can Do Now (That Wasn't Possible Before)

- **Mix poster sizes in one email** — landscape hero row on top, vertical thumbnails below
- **Show or hide genre tags and titles** — toggle per section, not baked into the block
- **Place genre above or below the poster** — useful for different visual treatments
- **Add "Watch Now" buttons to individual posters** — not just a section-level CTA
- **Left-align or center metadata text** — match the design intent per section
- **Use the same block for hand-picked and algorithm content** — no block-switching required

---

## Cheat Sheet: Common Scenarios

### A. API grid with genre tags (most common)

```
grid_api_items   = result.containers[0].items
grid_layout      = "3v"
grid_show_metadata = "true"
grid_meta_align  = "center"
grid_utm_params  = utm
→ poster_grid
```

### B. Manual curated grid (editorial picks)

```
grid_layout      = "2l"
grid_show_metadata = "false"
grid_item_1_img  = "https://..."
grid_item_1_url  = "https://..."
grid_item_2_img  = "https://..."
grid_item_2_url  = "https://..."
→ poster_grid
```

### C. API grid with per-poster buttons

```
grid_api_items   = result.containers[0].items
grid_layout      = "2v"
grid_show_metadata = "true"
grid_utm_params  = utm
grid_item_1_cta_label = "Watch Now"
grid_item_1_cta_url   = "https://..."
grid_item_2_cta_label = "Watch Now"
grid_item_2_cta_url   = "https://..."
→ poster_grid
```

---

## Quick Variable Reference

### Grid Configuration

| Variable | What it controls | Options | Default |
|---|---|---|---|
| `grid_layout` | Poster size for all rows | `3v`  `2v`  `1l`  `2l` | `3v` |
| `grid_rows` | Mix layouts per row | Comma-separated, e.g. `"1l,3v,2l"` | *(uses grid_layout)* |
| `grid_api_items` | Connect to API data | `result.containers[N].items` | — |
| `grid_utm_params` | UTM tracking string | Your UTM string | — |

### Metadata Display

| Variable | What it controls | Options | Default |
|---|---|---|---|
| `grid_show_metadata` | Show genre + title | `"true"` / `"false"` | `"false"` |
| `grid_show_genre` | Show genre only | `"true"` / `"false"` | follows metadata |
| `grid_show_title` | Show title only | `"true"` / `"false"` | follows metadata |
| `grid_meta_align` | Text alignment | `"left"` / `"center"` | `"left"` |
| `grid_meta_position` | Genre placement | `"below"` / `"above"` | `"below"` |

### Per-Item Content (repeat pattern for items 1–18)

| Variable | What it is |
|---|---|
| `grid_item_N_img` | Poster image URL |
| `grid_item_N_url` | Click-through link |
| `grid_item_N_subhead` | Title text (shown below poster) |
| `grid_item_N_genre` | Genre tags (shown with colored dots) |
| `grid_item_N_cta_label` | Button text (optional) |
| `grid_item_N_cta_url` | Button link (optional) |

> **Note:** When using API mode (`grid_api_items`), items 1–18 are auto-filled from the API response. You only need to set `grid_item_N_*` manually for hand-picked content or to override specific items (like adding CTA buttons).
