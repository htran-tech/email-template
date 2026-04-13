# Braze Upload Checklist - Quick Reference

## ✅ Upload Order (Follow This Sequence)

### Step 1: CSS Block (DO FIRST) 🔴 CRITICAL
```
Block Name: css_styles
File: styles/css-content-block.html
Status: [ ] Uploaded [ ] Tested
```

### Step 2: Core Blocks (In Any Order)

#### Block 2: Footer
```
Block Name: footer
File: content-blocks/core/footer.html
Status: [ ] Uploaded [ ] Tested
```

#### Block 3: Hero Basic ⭐ ENHANCED
```
Block Name: hero_basic
File: content-blocks/core/hero-basic.html
Status: [ ] Uploaded [ ] Tested
Note: Supports 3 variants + dual CTA
```

#### Block 4: Headline Body
```
Block Name: headline_body
File: content-blocks/core/headline-body.html
Status: [ ] Uploaded [ ] Tested
```

#### Block 5: 3-Column Grid ⭐ MOST USED
```
Block Name: poster_grid_3col
File: content-blocks/core/poster-grid-3col.html
Status: [ ] Uploaded [ ] Tested
```

#### Block 6: Single CTA
```
Block Name: cta_single
File: content-blocks/core/cta-single.html
Status: [ ] Uploaded [ ] Tested
```

#### Block 7: Double CTA
```
Block Name: cta_double
File: content-blocks/core/cta-double.html
Status: [ ] Uploaded [ ] Tested
```

### Step 3: Extended Blocks (Optional)

#### Block 8: Single Title Hero ⭐ ENHANCED
```
Block Name: single_title_hero
File: content-blocks/extended/single-title-hero.html
Status: [ ] Uploaded [ ] Tested
Note: Dual CTA support added
```

#### Block 9: 2-Col Vertical Grid
```
Block Name: poster_grid_2col_vertical
File: content-blocks/extended/poster-grid-2col-vertical.html
Status: [ ] Uploaded [ ] Tested
```

#### Block 10: 2-Col Landscape Grid
```
Block Name: poster_grid_2col_landscape
File: content-blocks/extended/poster-grid-2col-landscape.html
Status: [ ] Uploaded [ ] Tested
```

#### Block 11: Image Only
```
Block Name: img_only
File: content-blocks/extended/image-only.html
Status: [ ] Uploaded [ ] Tested
Note: Uses img_only (image_only was already taken)
```

---

## 🚀 Quick Test After Each Upload

After uploading each block, test it:

1. Create test campaign
2. Add this minimal template:
```liquid
{% content_block css_styles %}
<!-- Test your block here -->
{% content_block BLOCK_NAME %}
```
3. Send test email to yourself
4. Verify it works before moving to next block

---

## 📝 Copy-Paste Templates for Testing

### Test: Hero Standard (Dual CTA)
```liquid
{% assign hero_image_url = "https://picsum.photos/600/390" %}
{% assign hero_variant = "standard" %}
{% assign hero_orientation = "landscape" %}
{% assign headline_copy = "Test Hero" %}
{% assign body_copy = "Testing dual CTA" %}
{% assign cta_label = "Primary CTA" %}
{% assign cta_url = "https://tubitv.com" %}
{% assign cta2_label = "Secondary CTA" %}
{% assign cta2_url = "https://tubitv.com/browse" %}
{% content_block hero_basic %}
```

### Test: Hero Simple Overlay
```liquid
{% assign hero_image_url = "https://picsum.photos/600/600" %}
{% assign hero_variant = "simple-overlay" %}
{% assign hero_orientation = "portrait" %}
{% assign status_label = "Coming Soon" %}
{% assign show_backdrop_blur = true %}
{% content_block hero_basic %}
```

### Test: Hero Gradient Metadata
```liquid
{% assign hero_image_url = "https://picsum.photos/600/390" %}
{% assign hero_variant = "gradient-metadata" %}
{% assign hero_orientation = "landscape" %}
{% assign headline_copy = "Featured" %}
{% assign body_copy = "Check this out" %}
{% assign cta_label = "Watch" %}
{% assign cta_url = "https://tubitv.com" %}
{% assign cta2_label = "Browse" %}
{% assign cta2_url = "https://tubitv.com/browse" %}
{% content_block hero_basic %}
```

### Test: Single Title Hero (Dual CTA)
```liquid
{% assign title_image_url = "https://picsum.photos/600/800" %}
{% assign hero_orientation = "portrait" %}
{% assign title_name = "Test Movie" %}
{% assign title_year = "2024" %}
{% assign title_genre = "Action" %}
{% assign title_rating = "PG-13" %}
{% assign title_description = "This is a test description" %}
{% assign cta_label = "Watch Now" %}
{% assign cta_url = "https://tubitv.com" %}
{% assign cta2_label = "Add to List" %}
{% assign cta2_url = "https://tubitv.com/list" %}
{% content_block single_title_hero %}
```

---

## ⚠️ Common Mistakes to Avoid

❌ **WRONG Block Name:**
```liquid
{% content_block hero-basic %}  <!-- Hyphens don't work! -->
{% content_block heroBasic %}   <!-- camelCase doesn't work! -->
```

✅ **CORRECT Block Name:**
```liquid
{% content_block hero_basic %}  <!-- snake_case works! -->
```

❌ **WRONG CSS Reference:**
```liquid
{% content_block css_content_block %}  <!-- Wrong name! -->
{% content_block styles %}              <!-- Wrong name! -->
```

✅ **CORRECT CSS Reference:**
```liquid
{% content_block css_styles %}  <!-- Correct! -->
```

---

## 🎯 Success Criteria

After upload, verify:

- [ ] All content blocks show in Braze library
- [ ] CSS block loads without errors
- [ ] Test email sends successfully
- [ ] Preview renders correctly
- [ ] Mobile preview looks good
- [ ] No Liquid syntax errors
- [ ] Images load (if using real URLs)
- [ ] Variables render correctly
- [ ] Dual CTAs are side-by-side
- [ ] No missing content

---

## 📞 Need Help?

**Braze Support:**
- In-app chat in Braze dashboard
- support@braze.com
- [Braze Documentation](https://www.braze.com/docs)

**Project Documentation:**
- Full guide: `braze-import-guide.md`
- Usage guide: `docs/usage-guide.md`
- Variable reference: `docs/liquid-variables.md`

---

**Upload Started:** _______________
**Upload Completed:** _______________
**Tested By:** _______________
**Status:** ⬜ Ready for Production
