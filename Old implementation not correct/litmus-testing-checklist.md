# Litmus Testing Checklist for Hero Variants

## Pre-Test Setup
- [ ] Upload test-hero-variants.html to Litmus
- [ ] Select all recommended email clients (9+ clients)
- [ ] Include both light and dark mode tests
- [ ] Include both desktop and mobile clients

## Visual Verification Checklist

### All Hero Variants
- [ ] **Hero images load correctly** in all clients
- [ ] **Full-width heroes** (600px) display properly
- [ ] **Background images** show in supported clients
- [ ] **Gradient overlays** render with correct opacity
- [ ] **Text is readable** over images (contrast check)
- [ ] **Dark backgrounds** (#000000) don't invert in dark mode

### Variant 1: Standard Hero (Dual CTA)
- [ ] **Dual CTAs side-by-side** on desktop
- [ ] **Equal button widths** (50% each)
- [ ] **5px gap between buttons** visible
- [ ] **Primary CTA** has blue background (#00a8e1)
- [ ] **Secondary CTA** has white background
- [ ] **Button text** is black and readable
- [ ] **Buttons stack vertically** on mobile
- [ ] **Gradient overlay** is light (0.2-0.6 opacity)
- [ ] **Text shadow** makes headline readable

### Variant 2: Simple Overlay
- [ ] **Status label** ("Coming Soon") displays
- [ ] **Backdrop blur** works (Safari/modern browsers only)
- [ ] **Fallback background** works when blur unsupported
- [ ] **Minimal design** - no other text visible
- [ ] **Label centered** at top of hero
- [ ] **Landscape aspect** (~390px height) correct

### Variant 3: Gradient Metadata
- [ ] **Hero image** has gradient but no text
- [ ] **Metadata section below** hero is visible
- [ ] **Headline** renders correctly
- [ ] **Body copy** has line-height 1.2
- [ ] **Dual CTAs** side-by-side in metadata section
- [ ] **Black background** (#000000) on metadata section
- [ ] **Buttons stack** on mobile

## Mobile-Specific Checks (< 480px)

### Responsive Behavior
- [ ] **All buttons** become full-width
- [ ] **Dual CTAs stack** vertically
- [ ] **Touch targets** are 44px+ height
- [ ] **Font sizes** scale appropriately
- [ ] **Images** scale to device width
- [ ] **No horizontal scrolling** occurs
- [ ] **Spacing** looks balanced

### Mobile Clients to Check
- [ ] Gmail iOS App
- [ ] Gmail Android App
- [ ] Apple Mail iOS 15+
- [ ] Samsung Email Android
- [ ] Outlook iOS App

## Email Client-Specific Issues

### Gmail
- [ ] Background images display (CSS background-image)
- [ ] Gradient overlays render
- [ ] Dual CTAs don't break
- [ ] Dark mode: colors don't invert
- [ ] Mobile app: buttons stack properly

### Outlook (Windows Desktop)
- [ ] Background images show OR fallback works
- [ ] VML fallbacks render (if implemented)
- [ ] Table layouts don't break
- [ ] Buttons maintain proper spacing
- [ ] MSO conditional comments work

### Apple Mail
- [ ] Dark mode: #000000 stays black (doesn't invert)
- [ ] Backdrop blur shows on macOS/iOS
- [ ] Gradient overlays render smoothly
- [ ] Text remains white in dark mode
- [ ] CTA colors don't invert

### Outlook.com / Outlook 365
- [ ] Background images display
- [ ] Buttons render correctly
- [ ] No extra spacing issues
- [ ] Links are clickable
- [ ] Colors match design

## Dark Mode Verification

### Colors to Check:
- [ ] Background: #000000 (black) - doesn't invert
- [ ] Text: #ffffff (white) - stays visible
- [ ] Secondary text: #cccccc (gray) - readable
- [ ] Primary CTA: #00a8e1 (blue) - stays blue
- [ ] Secondary CTA: #ffffff (white) - adjusts to #e0e0e0

### Dark Mode Clients:
- [ ] Apple Mail (macOS) - automatic dark mode
- [ ] Apple Mail (iOS 15+) - automatic
- [ ] Gmail (iOS/Android) - manual toggle
- [ ] Outlook (Windows) - check both modes

## CSS/HTML Validation

### Code Analysis Tab Review:
- [ ] Check for unsupported CSS properties
- [ ] Review any HTML validation warnings
- [ ] Verify alt text on all images
- [ ] Check file size (should be < 102KB)
- [ ] Review link validation results

### Common Issues to Watch:
- [ ] `backdrop-filter` flagged as unsupported (expected - has fallback)
- [ ] `background-image` warnings for Outlook (expected - has VML)
- [ ] Media query support varies by client
- [ ] Some clients strip `<style>` blocks

## Performance Checks

- [ ] **File size** under 102KB (Gmail clipping)
- [ ] **Image URLs** are https:// (not file://)
- [ ] **Load time** acceptable in all clients
- [ ] **No broken images** (test with real URLs)

## Cross-Client Consistency

### What Should Be Consistent:
- [ ] Layout structure
- [ ] Button colors and styles
- [ ] Text hierarchy
- [ ] Spacing and padding
- [ ] Brand colors (#00a8e1)

### What May Vary (Expected):
- [ ] Backdrop blur (modern browsers only)
- [ ] Background images (Outlook limitations)
- [ ] Font rendering (system fonts differ)
- [ ] Exact gradient smoothness

## Final Checklist

- [ ] All 3 hero variants tested
- [ ] Desktop AND mobile versions reviewed
- [ ] Dark mode tested in supporting clients
- [ ] No critical rendering issues found
- [ ] Dual CTAs work in all clients
- [ ] Buttons are clickable (not broken)
- [ ] Text is readable in all scenarios
- [ ] Screenshot results saved/documented

## Issue Documentation

If issues found, document:
- **Client:** Which email client(s)
- **Issue:** Description of the problem
- **Severity:** Critical / High / Medium / Low
- **Screenshot:** Litmus screenshot link
- **Fix needed:** What needs to change

## Next Steps After Litmus

1. **Document all findings** in a shared doc/sheet
2. **Prioritize issues** (critical rendering bugs first)
3. **Create fix plan** for any failures
4. **Re-test** after implementing fixes
5. **Get stakeholder approval** on test results
6. **Proceed to Braze upload** once tests pass

---

**Test Date:** _______________
**Tester:** _______________
**Litmus Account:** _______________
**Test ID:** _______________

**Overall Status:** ⬜ Pass | ⬜ Pass with Minor Issues | ⬜ Fail (needs fixes)
