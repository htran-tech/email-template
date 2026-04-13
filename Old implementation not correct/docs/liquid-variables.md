# Liquid Variables Reference

## Overview

This document defines the standardized Liquid variable naming conventions and patterns used across all Braze Content Blocks in the email template system.

## Naming Conventions

### General Rules
- Use `snake_case` for all variable names
- Use descriptive, self-documenting names
- Prefix related variables consistently (e.g., `cta_`, `hero_`, `poster_`)
- Boolean flags should be prefixed with `show_` or `enable_`
- URLs should be suffixed with `_url`
- Labels/text should be suffixed with `_label` or `_copy`

### Variable Scoping
**IMPORTANT**: All variables should be reset at the end of each content block to prevent carryover to subsequent blocks.

```liquid
{% comment %} Reset variables at end of block {% endcomment %}
{% assign headline_copy = nil %}
{% assign body_copy = nil %}
{% assign cta_label = nil %}
{% assign cta_url = nil %}
```

## Common Variable Patterns

### Text Content
```liquid
{% assign headline_copy = "Your Headline Here" %}
{% assign body_copy = "Your body text here" %}
{% assign preview_text = "Email preview text" %}
```

### Links and URLs
```liquid
{% assign cta_url = "https://tubitv.com/..." %}
{% assign headline_url = "https://tubitv.com/..." %}
{% assign hero_image_url = "https://cms.tubitv.com/..." %}
```

### CTA Buttons
```liquid
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta_style = "primary" %}  {# Options: primary, secondary, dark, or hex color #}
{% assign cta_width = "fixed" %}    {# Options: full, fixed, auto #}
```

### Optional Features
```liquid
{% assign show_metadata = true %}       {# Show/hide poster metadata #}
{% assign enable_tracking = true %}     {# Enable/disable click tracking #}
{% assign show_headline = true %}       {# Show/hide headline #}
```

### Layout Options
```liquid
{% assign text_align = "center" %}      {# Options: center, left, right #}
{% assign hero_layout = "center" %}     {# Hero text overlay position #}
{% assign item_count = 6 %}             {# Number of items to display #}
```

### Localization
```liquid
{% assign language = "en" %}            {# ISO language code #}
{% assign country = "US" %}             {# ISO country code #}
```

## Data Types and Formats

### String
Most variables are strings. Use double quotes.
```liquid
{% assign headline_copy = "Watch New Movies" %}
```

### Boolean
Use `true` or `false` (no quotes).
```liquid
{% assign show_metadata = true %}
{% assign enable_tracking = false %}
```

### Number
Use integers or floats without quotes.
```liquid
{% assign item_count = 6 %}
{% assign font_size = 24 %}
```

### URL
Full absolute URLs including protocol.
```liquid
{% assign cta_url = "https://tubitv.com/home" %}
```

### Color
Hex color codes with # or predefined color names.
```liquid
{% assign cta_color = "#00a8e1" %}
{% assign cta_style = "primary" %}
```

## Default Values and Fallbacks

Use the `default` filter to provide fallback values:

```liquid
{% assign headline_copy = headline_copy | default: "Welcome to Tubi" %}
{% assign show_metadata = show_metadata | default: true %}
{% assign item_count = item_count | default: 6 %}
```

## Conditional Rendering

Show/hide content based on variable presence:

```liquid
{% if headline_copy and headline_copy != "" %}
  <h2>{{headline_copy}}</h2>
{% endif %}

{% if cta_label and cta_url %}
  <a href="{{cta_url}}">{{cta_label}}</a>
{% endif %}
```

## UTM Parameters

Dynamic UTM parameter construction:

```liquid
{% assign utm_source = "braze" %}
{% assign utm_medium = "email" %}
{% assign utm_campaign = campaign_name %}
{% assign utm_content = content_block_name %}

{% capture tracking_url %}{{base_url}}?utm_source={{utm_source}}&utm_medium={{utm_medium}}&utm_campaign={{utm_campaign}}{% endcapture %}
```

## API Content Variables

For dynamic content from APIs:

```liquid
{% assign api_endpoint = "https://api.tubitv.com/content/curated" %}
{% assign container_id = "trending_movies" %}
{% assign item_count = 6 %}
```

## Content Block Specific Variables

### Headline + Body Block
```liquid
{% assign headline_copy = "Your Headline" %}
{% assign headline_url = "" %}              {# Optional link #}
{% assign body_copy = "Your body text" %}
{% assign text_align = "center" %}
```

### CTA Button Block
```liquid
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta_style = "primary" %}
{% assign cta_width = "fixed" %}
{% assign enable_tracking = true %}
```

### Double CTA Block
```liquid
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta_style = "primary" %}

{% assign cta2_label = "Browse All" %}
{% assign cta2_url = "https://tubitv.com/..." %}
{% assign cta2_style = "secondary" %}
```

### Poster Grid 3-Column Block
```liquid
{% assign api_endpoint = "https://api.tubitv.com/..." %}
{% assign container_id = "trending_movies" %}
{% assign item_count = 6 %}
{% assign show_metadata = true %}
{% assign headline_copy = "" %}             {# Optional #}
{% assign body_copy = "" %}                 {# Optional #}
{% assign cta_label = "" %}                 {# Optional #}
{% assign cta_url = "" %}                   {# Optional #}
{% assign enable_tracking = true %}
```

### Hero Block (Enhanced with Variants)
```liquid
{% assign hero_image_url = "https://cms.tubitv.com/..." %}
{% assign hero_variant = "standard" %}      {# Options: standard, simple-overlay, gradient-metadata #}
{% assign hero_orientation = "landscape" %} {# Options: portrait, landscape #}
{% assign hero_layout = "center" %}         {# Options: center, left, right (for standard variant) #}
{% assign headline_copy = "Your Headline" %}
{% assign body_copy = "Your body text" %}
{% assign status_label = "Coming Soon" %}   {# For simple-overlay variant #}
{% assign show_backdrop_blur = true %}      {# Enable backdrop blur effect #}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta2_label = "Browse All" %}      {# Optional second CTA #}
{% assign cta2_url = "https://tubitv.com/..." %}  {# Optional second CTA URL #}
```

**Hero Variant Options:**
- **standard**: Text overlaid on hero image with gradient (current default)
- **simple-overlay**: Minimal status label only, clean hero image
- **gradient-metadata**: Gradient on image, all metadata below image

**Orientation Impact:**
- **portrait**: ~600px height, suitable for vertical movie posters
- **landscape**: ~390px height, suitable for horizontal banners

### Single Title Promo Hero Block
```liquid
{% assign title_image_url = "https://cms.tubitv.com/..." %}
{% assign hero_variant = "v1" %}            {# Options: v1, v2a, v2b, v3, v4 #}
{% assign hero_orientation = "portrait" %}  {# Options: portrait, landscape #}
{% assign color_mode = "dark" %}            {# Options: dark, light #}
{% assign status_label = "Trailer" %}       {# Optional badge (e.g., "Trailer", "New", "Coming Soon") #}
{% assign show_backdrop_blur = true %}      {# Backdrop blur on status badge #}
{% assign title_name = "Movie Title" %}
{% assign title_year = "2024" %}
{% assign title_genre = "Action" %}
{% assign title_rating = "PG-13" %}
{% assign title_description = "Brief description of the title..." %}
{% assign headline_copy = "" %}             {# Optional override for title_name #}
{% assign body_copy = "" %}                 {# Optional override for title_description #}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta2_label = "Add to List" %}    {# Optional second CTA #}
{% assign cta2_url = "https://tubitv.com/..." %}  {# Optional second CTA URL #}
{% assign bg_asset_base_url = "https://cdn.tubitv.com/email-assets/hero-bg" %}  {# CDN base for bg treatments #}
{% assign tubi_logo_url = "https://cdn.tubitv.com/email-assets/tubi-logo-white.png" %}  {# Tubi logo asset #}
```

**Variant Options (Figma mapping):**

| Value | Figma Name | Visual Treatment |
|-------|-----------|-----------------|
| `v1` | SingleTitleHeader_1 | Clean solid gradient background |
| `v2a` | SingleTitleHeader_2A | Curved/wavy arc at top edge |
| `v2b` | SingleTitleHeader_2B | Pinched/tapered sides with glow |
| `v3` | SingleTitleHeader_3 | Wide side-curve decorations |
| `v4` | SingleTitleHeader_4 | Yellow/gold border frame |

**Color Mode:**
- **dark** (default): `#0a0a0a` metadata bg, `#ffffff` text, `#ffffff` secondary CTA
- **light**: `#ffffff` metadata bg, `#1a1a1a` text, `#1a1a1a` secondary CTA

**Background Asset URL** is auto-computed:
`{bg_asset_base_url}/single-title-bg-{hero_variant}-{hero_orientation}.png`

### Footer Block
```liquid
{% assign language = "en" %}
{% assign country = "US" %}
```

## Manual Content Arrays

For manually curated poster grids:

```liquid
{% assign posters = "poster1.jpg,poster2.jpg,poster3.jpg" | split: "," %}
{% assign poster_urls = "url1,url2,url3" | split: "," %}
{% assign poster_titles = "Title 1,Title 2,Title 3" | split: "," %}
```

Iterate through arrays:
```liquid
{% for poster in posters %}
  <img src="{{poster}}" alt="{{poster_titles[forloop.index0]}}">
{% endfor %}
```

## Reserved Variable Names

The following variable names are reserved and should not be used for custom purposes:

- `email_subject`
- `preview_text`
- `unsubscribe_url` (Braze system tag)
- `view_in_browser_url` (Braze system tag)
- `user_id` (Braze user attribute)
- Any Braze custom attribute names

## Validation and Testing

When testing Liquid variables:
1. Test with all variables present
2. Test with optional variables missing
3. Test with empty string values
4. Test with invalid data types
5. Test variable scoping (ensure no carryover between blocks)

## Best Practices

1. **Always provide defaults** for optional variables
2. **Check for existence** before rendering content
3. **Reset variables** at the end of each content block
4. **Use consistent naming** across all blocks
5. **Document expected data types** for each variable
6. **Validate URLs** before rendering links
7. **Test edge cases** (very long text, special characters, etc.)
8. **Use comments** to explain complex Liquid logic

## Example: Complete Block with Variables

```liquid
{% comment %} Set variables {% endcomment %}
{% assign headline_copy = headline_copy | default: "" %}
{% assign body_copy = body_copy | default: "" %}
{% assign cta_label = cta_label | default: "" %}
{% assign cta_url = cta_url | default: "" %}
{% assign text_align = text_align | default: "center" %}

{% comment %} Render content {% endcomment %}
{% if headline_copy != "" %}
  <h2 style="text-align: {{text_align}};">{{headline_copy}}</h2>
{% endif %}

{% if body_copy != "" %}
  <p style="text-align: {{text_align}};">{{body_copy}}</p>
{% endif %}

{% if cta_label != "" and cta_url != "" %}
  <a href="{{cta_url}}" class="cta-button">{{cta_label}}</a>
{% endif %}

{% comment %} Reset variables {% endcomment %}
{% assign headline_copy = nil %}
{% assign body_copy = nil %}
{% assign cta_label = nil %}
{% assign cta_url = nil %}
{% assign text_align = nil %}
```

---

**Last Updated**: March 19, 2026
