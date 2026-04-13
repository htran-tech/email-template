# Email Template System - Usage Guide

## Overview

This guide explains how to use the modular content block system to build email campaigns in Braze without touching HTML code. The system consists of reusable Content Blocks that you combine to create complete emails.

## Quick Start

### Basic Email Structure

Every email follows this pattern:

1. **Start with the boilerplate** (`examples/boilerplate.html`)
2. **Add CSS Content Block** reference at the top
3. **Compose content blocks** in desired order
4. **End with Footer block**

### Minimum Required Elements

```html
<!DOCTYPE html...>
<head>
  {{content_blocks.${css_styles}}}
</head>
<body>
  <table class="email-container">
    <!-- Your content blocks here -->
    {{content_blocks.${footer}}}
  </table>
</body>
```

## Content Block Library

### Core Blocks (MVP)

| Block Name | File | Priority | Use Case |
|------------|------|----------|----------|
| 3-Column Poster Grid | `poster-grid-3col.html` | HIGHEST | Main content showcases |
| Headline + Body | `headline-body.html` | HIGH | Section headers, messaging |
| Single CTA | `cta-single.html` | HIGH | Primary call-to-action |
| Double CTA | `cta-double.html` | MEDIUM | Choice-based actions |
| Footer | `footer.html` | HIGH | Required in all emails |
| Hero Basic | `hero-basic.html` | MEDIUM | Email headers, featured content |

### Extended Blocks

| Block Name | File | Use Case |
|------------|------|----------|
| 2-Col Vertical Grid | `poster-grid-2col-vertical.html` | Larger poster displays |
| 2-Col Landscape Grid | `poster-grid-2col-landscape.html` | Landscape content |
| Image Only | `image-only.html` | Custom graphics, banners |
| Single Title Hero | `single-title-hero.html` | Title spotlights (5 Figma variants) |

## Building an Email Campaign

### Step 1: Choose Your Layout Pattern

Common layout patterns:

**Pattern A: Simple Marketing Email**
1. Hero Block
2. Headline + Body
3. 3-Column Poster Grid
4. Single CTA
5. Footer

**Pattern B: Content Discovery**
1. Headline + Body
2. 3-Column Poster Grid (Container 1)
3. Headline + Body
4. 3-Column Poster Grid (Container 2)
5. Single CTA
6. Footer

**Pattern C: Title Spotlight**
1. Single Title Hero
2. Headline + Body
3. 3-Column Poster Grid (Related titles)
4. Footer

### Step 2: Set Up Variables

Before each content block, define the Liquid variables it needs:

```liquid
{% comment %} Configure poster grid {% endcomment %}
{% assign headline_copy = "Trending This Week" %}
{% assign body_copy = "Check out what everyone's watching" %}
{% assign poster_images = "img1.jpg,img2.jpg,img3.jpg,img4.jpg,img5.jpg,img6.jpg" %}
{% assign poster_urls = "url1,url2,url3,url4,url5,url6" %}
{% assign item_count = 6 %}
{% assign show_metadata = true %}

{{content_blocks.${poster_grid_3col}}}
```

### Step 3: Add Content Blocks

Reference blocks using the Braze Content Block tag:

```liquid
{{content_blocks.${block_name}}}
```

### Step 4: Preview and Test

1. Use Braze preview mode to see your email
2. Send test emails to multiple email clients
3. Check mobile responsive behavior
4. Verify all links work correctly

## Variable Configuration Guide

### Required vs Optional Variables

**Required Variables** must be set or the block won't render:
- `cta_label` and `cta_url` (for CTA blocks)
- `image_url` (for image blocks)
- `hero_image_url` (for hero blocks)

**Optional Variables** enhance the block but aren't required:
- `headline_copy`, `body_copy` (add context)
- `show_metadata` (toggle metadata display)
- `enable_tracking` (toggle UTM tracking)

### Setting Variables

Always assign variables **before** the content block:

```liquid
{% assign headline_copy = "Your Headline" %}
{% assign body_copy = "Your body text" %}
{{content_blocks.${headline_body}}}
```

### Variable Scoping Rules

**Important:** Variables automatically reset after each content block. You must reassign them for each block.

**Wrong:**
```liquid
{% assign headline_copy = "Section 1" %}
{{content_blocks.${headline_body}}}

{{content_blocks.${headline_body}}}  <!-- headline_copy is now nil -->
```

**Correct:**
```liquid
{% assign headline_copy = "Section 1" %}
{{content_blocks.${headline_body}}}

{% assign headline_copy = "Section 2" %}
{{content_blocks.${headline_body}}}
```

## Working with Poster Grids

### Manual Content (Array Method)

For curated content, provide comma-separated values:

```liquid
{% assign poster_images = "https://cdn.tubitv.com/img1.jpg,https://cdn.tubitv.com/img2.jpg,https://cdn.tubitv.com/img3.jpg" %}
{% assign poster_urls = "https://tubitv.com/title1,https://tubitv.com/title2,https://tubitv.com/title3" %}
{% assign poster_titles = "Movie Title 1,Movie Title 2,Movie Title 3" %}
{% assign poster_years = "2023,2024,2022" %}
{% assign poster_genres = "Action,Comedy,Drama" %}
{% assign item_count = 3 %}
{% assign show_metadata = true %}

{{content_blocks.${poster_grid_3col}}}
```

### API-Powered Content

For dynamic content from your API:

```liquid
{% assign api_endpoint = "https://api.tubitv.com/content/curated" %}
{% assign container_id = "trending_movies" %}
{% assign item_count = 6 %}
{% assign show_metadata = true %}

{{content_blocks.${poster_grid_3col}}}
```

**Note:** API integration requires backend implementation. The block will render a placeholder until the API is connected.

### ⚠️ Layout Constraint: 4-Row Maximum

**IMPORTANT:** Don't exceed 4 rows for singular modular stacked layouts as email will become too lengthy (per Figma design standards).

For 3-column grids, this means:
- ✅ **Recommended:** 3, 6, 9, or 12 items (1-4 rows)
- ⚠️ **Avoid:** 15+ items (5+ rows) in a single grid

**Solution for longer content:** Break into multiple sections with headlines between grids.

```liquid
{% comment %} Good: Separated into sections {% endcomment %}
{% assign headline_copy = "Action Movies" %}
{{content_blocks.${headline_body}}}

{% assign item_count = 6 %}  <!-- 2 rows -->
{{content_blocks.${poster_grid_3col}}}

{% assign headline_copy = "Comedy Movies" %}
{{content_blocks.${headline_body}}}

{% assign item_count = 6 %}  <!-- 2 rows -->
{{content_blocks.${poster_grid_3col}}}
```

## Hero Variant Selection Guide

The Hero Basic block supports three layout variants to match different design needs:

### Variant 1: Standard (Default)
**Use when:** You need text overlaid directly on the hero image

```liquid
{% assign hero_image_url = "https://cdn.tubitv.com/hero.jpg" %}
{% assign hero_variant = "standard" %}
{% assign hero_layout = "center" %}  {# center, left, or right #}
{% assign hero_orientation = "landscape" %}
{% assign headline_copy = "New Movies This Week" %}
{% assign body_copy = "Stream thousands of titles" %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta2_label = "Browse All" %}  {# Optional dual CTA #}
{% assign cta2_url = "https://tubitv.com/..." %}
{{content_blocks.${hero_basic}}}
```

**Best for:** Feature announcements, marketing headers, promotional content

### Variant 2: Simple Overlay
**Use when:** You want a clean hero image with minimal text

```liquid
{% assign hero_image_url = "https://cdn.tubitv.com/hero.jpg" %}
{% assign hero_variant = "simple-overlay" %}
{% assign hero_orientation = "portrait" %}  {# portrait or landscape #}
{% assign status_label = "Coming Soon" %}
{% assign show_backdrop_blur = true %}  {# Optional blur effect #}
{{content_blocks.${hero_basic}}}
```

**Best for:** Title announcements, "coming soon" banners, visual-first content

### Variant 3: Gradient Metadata
**Use when:** You want the hero image separated from metadata content

```liquid
{% assign hero_image_url = "https://cdn.tubitv.com/hero.jpg" %}
{% assign hero_variant = "gradient-metadata" %}
{% assign hero_orientation = "landscape" %}
{% assign headline_copy = "Featured Collection" %}
{% assign body_copy = "Explore curated content" %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/..." %}
{% assign cta2_label = "Learn More" %}
{% assign cta2_url = "https://tubitv.com/..." %}
{{content_blocks.${hero_basic}}}
```

**Best for:** Collection showcases, editorial content, content with descriptions

### Hero Orientation Options

**Portrait** (~600px height):
- Best for movie/show posters
- Vertical aspect ratio
- More prominent visual impact

**Landscape** (~390px height):
- Best for banner-style content
- Horizontal aspect ratio
- More compact, efficient use of space

### Dual CTA Support

All hero variants support dual CTAs (side-by-side buttons):

```liquid
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/watch" %}
{% assign cta2_label = "Browse All" %}
{% assign cta2_url = "https://tubitv.com/browse" %}
```

**Mobile behavior:** Buttons stack vertically on mobile devices.

## Single Title Promo Hero Variant Guide

The Single Title Hero block supports 5 decorative background variants from the Figma design, each with portrait/landscape orientations, dark/light color modes, and optional status badges.

### Variant Overview

| Variant | Name | Best For |
|---------|------|----------|
| `v1` | Clean | Standard title promos, minimal design |
| `v2a` | Wave Top | High-impact launches, featured content |
| `v2b` | Pinched Sides | Premium feel, special events |
| `v3` | Side Curves | Editorial spotlights, curated picks |
| `v4` | Border Frame | Award-winning titles, special editions |

### Basic Usage

```liquid
{% assign title_image_url = "https://cdn.tubitv.com/poster.jpg" %}
{% assign hero_variant = "v1" %}
{% assign hero_orientation = "portrait" %}
{% assign title_name = "Sidelined: The QB and Me" %}
{% assign title_year = "2024" %}
{% assign title_genre = "Romance" %}
{% assign title_rating = "PG-13" %}
{% assign title_description = "A star quarterback and an aspiring journalist..." %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/movies/12345" %}
{% assign cta2_label = "Add to My List" %}
{% assign cta2_url = "https://tubitv.com/list/add/12345" %}
{{content_blocks.${single_title_hero}}}
```

### With Status Badge (Banner Sub-type)

```liquid
{% assign title_image_url = "https://cdn.tubitv.com/poster.jpg" %}
{% assign hero_variant = "v2a" %}
{% assign hero_orientation = "portrait" %}
{% assign status_label = "Trailer" %}
{% assign show_backdrop_blur = true %}
{% assign title_name = "New Movie Title" %}
{% assign cta_label = "Watch Trailer" %}
{% assign cta_url = "https://tubitv.com/trailer/12345" %}
{{content_blocks.${single_title_hero}}}
```

### Light Mode

```liquid
{% assign title_image_url = "https://cdn.tubitv.com/poster.jpg" %}
{% assign hero_variant = "v3" %}
{% assign hero_orientation = "portrait" %}
{% assign color_mode = "light" %}
{% assign title_name = "Comedy Title" %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/movies/67890" %}
{{content_blocks.${single_title_hero}}}
```

### Landscape Orientation

```liquid
{% assign title_image_url = "https://cdn.tubitv.com/landscape-hero.jpg" %}
{% assign hero_variant = "v1" %}
{% assign hero_orientation = "landscape" %}
{% assign title_name = "Action Movie" %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/movies/11111" %}
{{content_blocks.${single_title_hero}}}
```

### Asset Requirements

Each variant requires pre-exported background treatment images uploaded to CDN:
- 10 images total: 5 variants x 2 orientations
- Format: `single-title-bg-{variant}-{orientation}.png`
- Width: 600px, PNG with transparent poster area
- Set `bg_asset_base_url` to your CDN path (default: `https://cdn.tubitv.com/email-assets/hero-bg`)

## CTA Button Configuration

### Color Variants

```liquid
{% assign cta_style = "primary" %}   <!-- Blue background, black text -->
{% assign cta_style = "secondary" %} <!-- White background, black text -->
{% assign cta_style = "dark" %}      <!-- Black background, white text -->
{% assign cta_style = "#ff6600" %}   <!-- Custom hex color -->
```

### Width Options

```liquid
{% assign cta_width = "full" %}   <!-- 100% width (mobile-friendly) -->
{% assign cta_width = "fixed" %}  <!-- 200px min width -->
{% assign cta_width = "auto" %}   <!-- Fits content -->
```

### Button Alignment

```liquid
{% assign cta_align = "center" %}  <!-- Default -->
{% assign cta_align = "left" %}
{% assign cta_align = "right" %}
```

## UTM Tracking

UTM parameters are automatically added when `enable_tracking = true` (default).

### Default UTM Parameters

```liquid
{% assign utm_source = "braze" %}
{% assign utm_medium = "email" %}
{% assign utm_campaign = "email_campaign" %}
```

### Custom UTM Parameters

Override defaults before your content block:

```liquid
{% assign utm_campaign = "holiday_promo_2026" %}
{% assign utm_content = "hero_banner" %}
{{content_blocks.${hero_basic}}}
```

### Disable Tracking

```liquid
{% assign enable_tracking = false %}
{{content_blocks.${poster_grid_3col}}}
```

## Localization and Internationalization

The footer block automatically adjusts based on language and country:

```liquid
{% assign language = "en" %}  <!-- Options: en, es -->
{% assign country = "US" %}   <!-- Options: US, CA -->
{{content_blocks.${footer}}}
```

Supported combinations:
- `en` + `US` - English (United States)
- `en` + `CA` - English (Canada)
- `es` + `US` - Spanish (United States)

## Responsive Design Best Practices

### Mobile-First Approach

All blocks are designed mobile-first and automatically adapt:

**Desktop (600px):**
- 3-column grids show 3 posters per row
- Side-by-side CTA buttons
- Larger fonts and spacing

**Mobile (<480px):**
- Single column layout
- Stacked posters
- Stacked CTA buttons
- Optimized touch targets (44px minimum)

### Testing Mobile Behavior

Always test on actual devices:
- iOS Mail app
- Gmail app (iOS and Android)
- Samsung Email
- Outlook mobile

### Font Size Guidelines

- Headlines: 28-36px (desktop), 24-28px (mobile)
- Body copy: 16px (desktop), 15px (mobile)
- Metadata: 12-14px
- Footer: 11-12px

## Dark Mode Considerations

All blocks support dark mode with these defaults:

- Background: `#000000` (true black)
- Text: `#ffffff` (white) and `#cccccc` (light gray)
- Links: `#00a8e1` (Tubi blue)
- Borders: `#333333` (dark gray)

**Secondary CTA in Dark Mode:**
- Automatically adjusts to `#e0e0e0` to remain visible

### Testing Dark Mode

Test in these environments:
- Apple Mail (macOS, iOS) - automatic dark mode
- Gmail (iOS, Android) - manual dark mode toggle
- Outlook (Windows, Mac) - various dark mode behaviors

## File Size Optimization

**Gmail Clipping Warning:** Emails over 102KB get clipped.

### Size Budget

- CSS Content Block: <10KB
- Each content block: 2-5KB
- Total email: <100KB (safe threshold)

### Optimization Tips

1. **Minimize Content Blocks:** Use only what you need
2. **Optimize Images:** Use CDN URLs, not base64
3. **Remove Comments:** In production, strip `{% comment %}` blocks
4. **Compress HTML:** Remove extra whitespace

## Common Patterns and Examples

### Pattern: Marketing Campaign

```liquid
{% comment %} Hero Section {% endcomment %}
{% assign hero_image_url = "https://cdn.tubitv.com/hero.jpg" %}
{% assign headline_copy = "New Movies This Week" %}
{% assign body_copy = "Discover the latest additions" %}
{% assign cta_label = "Browse Now" %}
{% assign cta_url = "https://tubitv.com/new" %}
{{content_blocks.${hero_basic}}}

{% comment %} Featured Content {% endcomment %}
{% assign headline_copy = "Trending Now" %}
{% assign poster_images = "img1,img2,img3,img4,img5,img6" %}
{% assign poster_urls = "url1,url2,url3,url4,url5,url6" %}
{% assign item_count = 6 %}
{{content_blocks.${poster_grid_3col}}}

{% comment %} Footer {% endcomment %}
{% assign language = "en" %}
{% assign country = "US" %}
{{content_blocks.${footer}}}
```

### Pattern: Behavioral Email

```liquid
{% comment %} Personalized Headline {% endcomment %}
{% assign headline_copy = "Continue Watching" %}
{% assign body_copy = "Pick up where you left off" %}
{{content_blocks.${headline_body}}}

{% comment %} Continue Watching Grid {% endcomment %}
{% assign api_endpoint = "https://api.tubitv.com/user/continue-watching" %}
{% assign item_count = 3 %}
{{content_blocks.${poster_grid_3col}}}

{% comment %} Recommendations {% endcomment %}
{% assign headline_copy = "You Might Also Like" %}
{% assign api_endpoint = "https://api.tubitv.com/user/recommendations" %}
{% assign item_count = 6 %}
{{content_blocks.${poster_grid_3col}}}

{{content_blocks.${footer}}}
```

### Pattern: Title Spotlight

```liquid
{% comment %} Featured Title {% endcomment %}
{% assign title_image_url = "https://cdn.tubitv.com/title-hero.jpg" %}
{% assign title_name = "Amazing Movie Title" %}
{% assign title_year = "2024" %}
{% assign title_genre = "Action, Adventure" %}
{% assign title_description = "An epic adventure awaits..." %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/movies/12345" %}
{{content_blocks.${single_title_hero}}}

{% comment %} Related Titles {% endcomment %}
{% assign headline_copy = "More Like This" %}
{% assign api_endpoint = "https://api.tubitv.com/related/12345" %}
{% assign item_count = 6 %}
{{content_blocks.${poster_grid_3col}}}

{{content_blocks.${footer}}}
```

## Troubleshooting

### Block Not Rendering

**Problem:** Content block doesn't appear in email.

**Solutions:**
1. Check that required variables are set
2. Verify content block name matches exactly
3. Ensure variables are assigned **before** the block
4. Check for typos in variable names

### Images Not Loading

**Problem:** Images broken or not showing.

**Solutions:**
1. Verify image URLs are absolute (include `https://`)
2. Check that images are hosted on accessible CDN
3. Test image URLs in browser first
4. Ensure alt text is provided for accessibility

### Spacing Issues

**Problem:** Too much or too little spacing between blocks.

**Solutions:**
1. Use spacer tables between blocks
2. Check padding values in content blocks
3. Test in preview mode before sending
4. Adjust margin variables for image blocks

### Dark Mode Problems

**Problem:** Text unreadable in dark mode.

**Solutions:**
1. Test in actual dark mode clients
2. Verify color contrast ratios
3. Use light text on dark backgrounds
4. Check secondary CTA colors

### UTM Parameters Not Working

**Problem:** Tracking parameters not appearing in links.

**Solutions:**
1. Ensure `enable_tracking = true`
2. Check that URLs don't have fragments (#)
3. Verify UTM variables are set before block
4. Test links in preview mode

### Variables Carrying Over

**Problem:** Previous block's variables appear in next block.

**Solutions:**
1. Variables automatically reset after each block
2. Always reassign variables for each block
3. Don't rely on values from previous blocks
4. Use unique variable names if needed

## Best Practices

### 1. Always Use the Boilerplate

Start every email with the standard boilerplate to ensure:
- Proper DOCTYPE and meta tags
- CSS content block reference
- Email client compatibility
- Preview text setup

### 2. Test Early and Often

- Preview in Braze before sending
- Send test emails to real email clients
- Test on mobile devices
- Verify links and tracking

### 3. Keep It Simple

- Use minimum blocks needed for your message
- Don't over-design
- Focus on clear calls-to-action
- Prioritize content over decoration

### 4. Maintain Consistency

- Use the same CTA styles across campaigns
- Keep spacing consistent
- Follow brand color guidelines
- Reuse successful patterns

### 5. Think Mobile-First

- Design for small screens first
- Use large, tappable buttons
- Keep copy concise
- Test on actual mobile devices

### 6. Monitor Performance

- Track email file size (<100KB)
- Monitor CTR by block type
- A/B test different layouts
- Iterate based on data

## Advanced Techniques

### Dynamic Personalization

Use Braze personalization tags with content blocks:

```liquid
{% assign headline_copy = "Hey {{${first_name}}}, Check This Out!" %}
{{content_blocks.${headline_body}}}
```

### Conditional Content

Show different content based on user attributes:

```liquid
{% if {{custom_attribute.${subscription_type}}} == "premium" %}
  {% assign headline_copy = "Exclusive Premium Content" %}
{% else %}
  {% assign headline_copy = "Trending Free Movies" %}
{% endif %}

{{content_blocks.${headline_body}}}
```

### A/B Testing Layouts

Test different block combinations:

**Variant A:**
```liquid
{{content_blocks.${hero_basic}}}
{{content_blocks.${poster_grid_3col}}}
```

**Variant B:**
```liquid
{{content_blocks.${headline_body}}}
{{content_blocks.${poster_grid_2col_vertical}}}
```

## Resources

- **Liquid Variables Reference:** See `liquid-variables.md`
- **Example Templates:** See `/examples/` directory
- **Braze Documentation:** [Braze Content Blocks](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/content_blocks/)
- **Litmus Testing:** [Litmus Email Testing](https://litmus.com/)

## Support

For questions or issues:
1. Check this guide first
2. Review example templates
3. Consult Liquid variables reference
4. Contact the CRM development team

---

**Last Updated:** March 19, 2026
**Version:** 1.0 (MVP Release)
