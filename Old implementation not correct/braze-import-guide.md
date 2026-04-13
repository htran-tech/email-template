# Braze Import Guide - Content Block Upload

## Overview
This guide walks through uploading all content blocks to Braze and creating your first email campaign.

## Prerequisites
- [ ] Braze account access with Content Block permissions
- [ ] All HTML files ready in `/content-blocks/` and `/styles/`
- [ ] Test images uploaded to CDN (if not using API)

---

## Phase 1: Upload CSS Content Block (CRITICAL - Do First)

### Step 1.1: Upload CSS Styles

1. **Navigate to Content Blocks:**
   - Braze Dashboard → **Templates & Media** → **Content Blocks Library**

2. **Create New Content Block:**
   - Click **"+ Create Content Block"** button
   - Choose **"HTML"** type

3. **Configure CSS Block:**
   - **Content Block Name:** `css_styles` (EXACT name - referenced in all templates)
   - **Content Block Tags:** Add tag "styles" for organization
   - **Description:** "Base CSS styles for all email templates - DO NOT DELETE"

4. **Copy CSS Content:**
   - Open: `/styles/css-content-block.html`
   - Copy ENTIRE contents (including `<style>` tags)
   - Paste into Braze content block editor

5. **Save:**
   - Click **"Save Content Block"**
   - Test that it saved correctly

**IMPORTANT:** This block MUST be named exactly `css_styles` because all templates reference:
```liquid
{% content_block css_styles %}
```

---

## Phase 2: Upload Core Content Blocks

Upload these 6 essential blocks in order:

### Block 1: Footer (HIGH PRIORITY)
- **Braze Name:** `footer`
- **File:** `/content-blocks/core/footer.html`
- **Tags:** core, footer
- **Description:** "Footer with app store links, social icons, legal copy"

### Block 2: Hero Basic (HIGH PRIORITY)
- **Braze Name:** `hero_basic`
- **File:** `/content-blocks/core/hero-basic.html`
- **Tags:** core, hero
- **Description:** "Enhanced hero with 3 variants (standard, simple-overlay, gradient-metadata), dual CTA support"

### Block 3: Headline + Body (HIGH PRIORITY)
- **Braze Name:** `headline_body`
- **File:** `/content-blocks/core/headline-body.html`
- **Tags:** core, text
- **Description:** "Headline and body copy block with alignment options"

### Block 4: 3-Column Poster Grid (HIGHEST PRIORITY)
- **Braze Name:** `poster_grid_3col`
- **File:** `/content-blocks/core/poster-grid-3col.html`
- **Tags:** core, grid
- **Description:** "3-column poster grid - most frequently used block"

### Block 5: Single CTA Button (HIGH PRIORITY)
- **Braze Name:** `cta_single`
- **File:** `/content-blocks/core/cta-single.html`
- **Tags:** core, cta
- **Description:** "Single call-to-action button with color variants"

### Block 6: Double CTA Buttons (MEDIUM PRIORITY)
- **Braze Name:** `cta_double`
- **File:** `/content-blocks/core/cta-double.html`
- **Tags:** core, cta
- **Description:** "Two side-by-side CTA buttons"

---

## Phase 3: Upload Extended Content Blocks (Optional)

Upload these 4 advanced blocks:

### Block 7: Single Title Hero
- **Braze Name:** `single_title_hero`
- **File:** `/content-blocks/extended/single-title-hero.html`
- **Tags:** extended, hero
- **Description:** "Featured title spotlight with metadata, dual CTA support"

### Block 8: 2-Column Vertical Grid
- **Braze Name:** `poster_grid_2col_vertical`
- **File:** `/content-blocks/extended/poster-grid-2col-vertical.html`
- **Tags:** extended, grid
- **Description:** "2-column vertical poster grid"

### Block 9: 2-Column Landscape Grid
- **Braze Name:** `poster_grid_2col_landscape`
- **File:** `/content-blocks/extended/poster-grid-2col-landscape.html`
- **Tags:** extended, grid
- **Description:** "2-column landscape poster grid"

### Block 10: Image Only
- **Braze Name:** `img_only`
- **File:** `/content-blocks/extended/image-only.html`
- **Tags:** extended, image
- **Description:** "Standalone clickable image block"
- **Note:** Uses `img_only` because `image_only` was already taken

---

## Phase 4: Create Your First Test Email

### Step 4.1: Create New Campaign

1. **Navigate to Campaigns:**
   - Braze Dashboard → **Campaigns** → **Create Campaign**

2. **Select Email:**
   - Click **"Email"** campaign type

3. **Configure Campaign:**
   - **Campaign Name:** "Test - Hero Variants"
   - **Description:** "Testing new hero block enhancements"

### Step 4.2: Build Email

1. **Compose Email:**
   - Click **"Edit Email Body"**

2. **Choose HTML Editor:**
   - Select **"HTML Editor"** (not Drag & Drop)

3. **Add Email Template:**
   - Copy template from `/examples/boilerplate.html` OR use this quick test:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Test Email</title>

  <!-- CSS Content Block Reference -->
  {% content_block css_styles %}
</head>
<body style="margin: 0; padding: 0; background-color: #000000;">

  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #000000;">
    <tr>
      <td align="center">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" class="email-container">

          <!-- TEST: Hero Basic with Dual CTA -->
          {% assign hero_image_url = "https://picsum.photos/600/600" %}
          {% assign hero_variant = "standard" %}
          {% assign hero_orientation = "portrait" %}
          {% assign headline_copy = "Test Hero Block" %}
          {% assign body_copy = "Testing dual CTA functionality" %}
          {% assign cta_label = "Watch Now" %}
          {% assign cta_url = "https://tubitv.com" %}
          {% assign cta2_label = "Browse All" %}
          {% assign cta2_url = "https://tubitv.com/browse" %}
          {% content_block hero_basic %}

          <!-- Footer -->
          {% assign language = "en" %}
          {% assign country = "US" %}
          {% content_block footer %}

        </table>
      </td>
    </tr>
  </table>

</body>
</html>
```

4. **Save Email:**
   - Click **"Done"** to save

### Step 4.3: Preview Email

1. **Click "Preview and Test":**
   - Located in email editor

2. **Preview Options:**
   - **Test User:** Select a test user or use "Custom User"
   - **Device:** Toggle between Desktop/Mobile/Tablet
   - **Email Client:** Preview rendering

3. **Check Variables:**
   - Verify all `{% assign %}` variables render correctly
   - Check that `{% content_block %}` tags load blocks
   - Ensure no Liquid syntax errors

### Step 4.4: Send Test Email

1. **Send Test:**
   - Click **"Send Test"** button in preview

2. **Enter Email Addresses:**
   - Add your email(s)
   - Add team members' emails
   - Separate with commas

3. **Send:**
   - Click **"Send Test"**
   - Check inbox within 1-2 minutes

---

## Phase 5: Test All Hero Variants

Create test emails for each variant:

### Test 1: Standard Hero (Dual CTA)
```liquid
{% assign hero_variant = "standard" %}
{% assign hero_orientation = "landscape" %}
{% assign hero_image_url = "https://picsum.photos/600/390" %}
{% assign hero_layout = "center" %}
{% assign headline_copy = "New This Week" %}
{% assign body_copy = "Stream thousands of movies free" %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/watch" %}
{% assign cta2_label = "Browse All" %}
{% assign cta2_url = "https://tubitv.com/browse" %}
{% content_block hero_basic %}
```

### Test 2: Simple Overlay
```liquid
{% assign hero_variant = "simple-overlay" %}
{% assign hero_orientation = "portrait" %}
{% assign hero_image_url = "https://picsum.photos/600/600" %}
{% assign status_label = "Coming Soon" %}
{% assign show_backdrop_blur = true %}
{% content_block hero_basic %}
```

### Test 3: Gradient Metadata
```liquid
{% assign hero_variant = "gradient-metadata" %}
{% assign hero_orientation = "landscape" %}
{% assign hero_image_url = "https://picsum.photos/600/390" %}
{% assign headline_copy = "Featured Collection" %}
{% assign body_copy = "Curated content just for you" %}
{% assign cta_label = "Explore Now" %}
{% assign cta_url = "https://tubitv.com/featured" %}
{% assign cta2_label = "See All" %}
{% assign cta2_url = "https://tubitv.com/browse" %}
{% content_block hero_basic %}
```

### Test 4: Single Title Hero (Dual CTA)
```liquid
{% assign title_image_url = "https://picsum.photos/600/800" %}
{% assign hero_orientation = "portrait" %}
{% assign title_name = "The Amazing Movie" %}
{% assign title_year = "2024" %}
{% assign title_genre = "Action, Adventure" %}
{% assign title_rating = "PG-13" %}
{% assign title_description = "An epic adventure that will keep you on the edge of your seat." %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com/movie/123" %}
{% assign cta2_label = "Add to List" %}
{% assign cta2_url = "https://tubitv.com/my-list/add/123" %}
{% content_block single_title_hero %}
```

---

## Phase 6: Testing Checklist

After uploading to Braze, verify:

### Content Block Verification
- [ ] All 10 content blocks uploaded successfully
- [ ] CSS block named exactly `css_styles`
- [ ] All block names match reference tags
- [ ] No Liquid syntax errors in blocks
- [ ] Block tags added for organization

### Email Campaign Testing
- [ ] Test email campaign created
- [ ] HTML editor used (not drag & drop)
- [ ] Email references `{% content_block css_styles %}`
- [ ] Preview shows correctly in Braze
- [ ] Test email sends successfully
- [ ] Email arrives in inbox

### Variable Testing
- [ ] All `{% assign %}` variables work
- [ ] Content blocks render correctly
- [ ] No Liquid parsing errors
- [ ] Optional variables work when empty
- [ ] Variable scoping/reset works

### Hero Variant Testing
- [ ] Standard variant displays correctly
- [ ] Simple overlay variant works
- [ ] Gradient metadata variant works
- [ ] Dual CTAs appear side-by-side
- [ ] Portrait orientation (600px) works
- [ ] Landscape orientation (390px) works

### Mobile Responsive Testing
- [ ] Preview in Braze mobile view
- [ ] Send test to mobile devices
- [ ] Buttons stack on mobile (<480px)
- [ ] Touch targets are 44px+
- [ ] Images scale properly

### Cross-Client Testing
- [ ] Gmail (web and mobile app)
- [ ] Apple Mail (iOS/macOS)
- [ ] Outlook (web/desktop)
- [ ] Yahoo Mail
- [ ] Dark mode in supported clients

---

## Common Issues & Solutions

### Issue: "Content Block Not Found" Error
**Cause:** Block name mismatch
**Fix:**
- Ensure Content Block name in Braze matches exactly
- Check for typos: `hero_basic` not `hero-basic` or `heroBasic`
- Name is case-sensitive

### Issue: CSS Not Loading
**Cause:** CSS block name incorrect
**Fix:**
- CSS block MUST be named `css_styles` (with underscore)
- Check it's referenced as `{% content_block css_styles %}`

### Issue: Variables Not Rendering
**Cause:** Liquid syntax error
**Fix:**
- Check for typos in variable names
- Ensure all `{% assign %}` tags are closed
- Use Braze preview to see Liquid errors

### Issue: Images Not Loading
**Cause:** Invalid image URLs or permissions
**Fix:**
- Use full absolute URLs: `https://cdn.tubitv.com/...`
- Ensure images are publicly accessible
- Check CDN CORS settings

### Issue: Dual CTAs Not Side-by-Side
**Cause:** CSS not loaded or mobile view
**Fix:**
- Verify CSS content block is loaded
- Check in desktop preview (mobile should stack)
- Inspect for CSS conflicts

### Issue: Content Block Changes Not Showing
**Cause:** Braze caching
**Fix:**
- Save content block
- Refresh email campaign editor
- Create new test send

---

## Best Practices

### Naming Conventions
✅ **DO:**
- Use snake_case: `hero_basic`, `poster_grid_3col`
- Be consistent across all blocks
- Use descriptive names

❌ **DON'T:**
- Use spaces: `hero basic`
- Use hyphens: `hero-basic` (Liquid doesn't support)
- Use camelCase: `heroBasic`

### Organization
- **Use Tags:** Tag blocks as "core", "extended", "hero", "grid", "cta"
- **Add Descriptions:** Helpful for team members
- **Version Control:** If updating, note version in description

### Testing Workflow
1. Upload CSS block first
2. Upload one content block at a time
3. Test each block individually
4. Then test combinations
5. Send test emails frequently

### Variable Management
- Always set defaults in content blocks: `| default: "value"`
- Reset variables at end of blocks: `{% assign var = nil %}`
- Document required vs optional variables

---

## Quick Reference: All Block Names

Copy this for easy reference:

```
CSS Block:
- css_styles

Core Blocks:
- footer
- hero_basic
- headline_body
- poster_grid_3col
- cta_single
- cta_double

Extended Blocks:
- single_title_hero
- poster_grid_2col_vertical
- poster_grid_2col_landscape
- img_only
```

---

## Next Steps After Upload

1. **Test All Variants:** Send test emails for each hero variant
2. **Team Review:** Share test emails with stakeholders
3. **Documentation:** Share usage guide with CRM team
4. **Training:** Schedule walkthrough for team members
5. **Production:** Create first real campaign
6. **Monitor:** Track performance and gather feedback

---

## Support Resources

**Braze Documentation:**
- [Content Blocks Guide](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/content_blocks/)
- [Liquid Templating](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/)
- [Email Best Practices](https://www.braze.com/docs/user_guide/message_building_by_channel/email/best_practices/)

**Project Documentation:**
- Usage Guide: `/docs/usage-guide.md`
- Variable Reference: `/docs/liquid-variables.md`
- Examples: `/examples/` folder

---

**Import Date:** _______________
**Imported By:** _______________
**Braze Account:** _______________
**Status:** ⬜ Complete | ⬜ In Progress | ⬜ Not Started
