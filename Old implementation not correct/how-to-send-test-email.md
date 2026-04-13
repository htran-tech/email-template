# How to Send Test Email in Braze - Step by Step

## Start Here

### Step 1: Create Campaign
1. Go to Braze Dashboard
2. Click **"Campaigns"** in left sidebar
3. Click **"+ Create Campaign"** button (top right)
4. Select **"Email"** from options

### Step 2: Name Your Campaign
1. **Campaign Name:** "Test - Hero Variants"
2. **Description:** "Testing new hero block enhancements"
3. Click **"Create Campaign"** or **"Next"**

### Step 3: Compose Email
1. Click **"Edit Email Body"** button
2. Choose **"HTML Editor"** (NOT Drag & Drop)
3. You'll see a code editor window
4. Copy everything from `braze-first-test.html`
5. Paste into the code editor
6. Click **"Done"** or **"Save"**

### Step 4: Fill Required Fields

You'll see these fields (fill them out):

**Display Info:**
```
From Display Name: Tubi
From Email: hello@tubitv.com (or your sending domain)
Subject Line: Test - Hero Variants
```

**Optional Fields:**
```
Reply-To: support@tubitv.com (where users' replies go)
Preview Text: Testing new hero blocks
```

### Step 5: Send Test Email ✨ THE IMPORTANT PART

Now look for the **"Preview and Test"** button:

**Location:** Usually top-right of the screen, near "Save" or "Next"

**Click it!** A new section will appear.

### Step 6: Enter Your Email

You should see:

**Option 1: Send Test Tab**
```
┌──────────────────────────────────────────┐
│ Send Test                                │
├──────────────────────────────────────────┤
│ Enter email addresses to send test to:  │
│                                          │
│ ┌──────────────────────────────────────┐ │
│ │ your.email@company.com               │ │
│ └──────────────────────────────────────┘ │
│                                          │
│ [ Send Test Email ]  ← CLICK THIS       │
└──────────────────────────────────────────┘
```

**Option 2: Test User Section**
```
Select a user to preview as (dropdown)
[ Send Test ] button
```

### Step 7: Click Send

1. Type your email: `your.email@company.com`
2. Click **"Send Test"** or **"Send Test Email"** button
3. You'll see confirmation: "Test email sent!"

### Step 8: Check Your Inbox

- Wait 1-2 minutes
- Check your inbox
- Check spam folder if you don't see it
- Open the email and review!

---

## 🎯 What Email Address to Use?

### For Testing: ANY email works!
```
✅ your.work@company.com
✅ your.personal@gmail.com
✅ teammate@company.com
✅ designer@agency.com
```

You can send to multiple addresses at once:
```
your@company.com, designer@agency.com, boss@company.com
```

### You DON'T Need:
- ❌ Email to be in Braze user database
- ❌ Special test user accounts
- ❌ Configured user segments
- ❌ Campaign targeting rules

**Test sends bypass all targeting rules!**

---

## 🔧 Troubleshooting

### "I don't see 'Preview and Test' button"

**Try these locations:**
1. Top-right corner of campaign editor
2. Near "Save Draft" button
3. In the "Review" or "Confirm" step
4. Look for icons: 👁️ ✉️ 🚀

**Still can't find it?**
- Make sure you saved the email body first
- Try refreshing the page
- Check if you're on "Compose" step vs "Target" step

### "Button is grayed out"

**Reasons:**
- Email body is empty → Add your HTML first
- Missing required fields → Fill out "Subject Line" and "From Email"
- Not saved yet → Click "Save Draft" first

**Fix:** Complete all required fields, then try again

### "Test email never arrived"

**Check:**
1. Spam/Junk folder
2. Email address spelling (typos?)
3. Your email server isn't blocking Braze
4. Wait 5 minutes (sometimes delayed)

**Try:**
- Send to a different email address
- Use Gmail or Yahoo (known to work)
- Check Braze status page for issues

### "Liquid syntax error"

**Means:**
- Something wrong in your HTML code
- Missing closing tags
- Content block not found

**Fix:**
1. Check Content Block names match exactly
2. Verify `css_styles` block exists
3. Look for red error messages in preview
4. Check all `{% assign %}` tags are closed

---

## 📧 Email Field Explanations

Here's what each field means:

### From Display Name
**What it is:** The name recipients see as sender
**Example:** "Tubi" or "Tubi Movies"
**Shows as:** "From: Tubi <hello@tubitv.com>"

### From Email Address
**What it is:** The email address sending the email
**Example:** "hello@tubitv.com"
**Must be:** A domain you own/verified in Braze

### Reply-To Address ← NOT FOR TEST EMAILS!
**What it is:** Where replies go if user hits "Reply"
**Example:** "support@tubitv.com"
**Used for:** Production emails, not test sends
**Can be:** Same as From Email or different

### BCC Address
**What it is:** Blind copy of every email sent
**Example:** "monitoring@tubitv.com"
**Used for:** Internal tracking (optional)

### Subject Line
**What it is:** Email subject line
**Example:** "New This Week on Tubi"
**Required:** Yes

### Preview Text (Preheader)
**What it is:** Text shown after subject in inbox
**Example:** "Stream these new movies free"
**Required:** No (but recommended)

---

## ✅ Quick Checklist

Before sending test:

- [ ] Campaign created
- [ ] HTML pasted into email body
- [ ] Email body saved
- [ ] Subject line filled in
- [ ] From email filled in
- [ ] Content blocks uploaded to Braze
- [ ] "Preview and Test" button clicked
- [ ] Your email address entered
- [ ] "Send Test" button clicked

---

## 🚀 Speed Run (Fast Method)

1. **Campaigns** → **+ Create** → **Email**
2. Name: "Test"
3. **Edit Email Body** → **HTML Editor**
4. Paste HTML → **Done**
5. Subject: "Test"
6. From: "Tubi" / "hello@tubitv.com"
7. **Preview and Test** → **Send Test**
8. Enter: your@email.com
9. **Send Test Email**
10. Check inbox!

**Time:** 3 minutes

---

## 💡 Pro Tips

### Send to Multiple People
```
you@company.com, designer@company.com, boss@company.com
```

### Test on Different Email Clients
Send to:
- Gmail: you@gmail.com
- Outlook: you@outlook.com
- Apple Mail: you@icloud.com
- Work email: you@company.com

### Mobile Testing
- Send to phone: your.mobile@gmail.com
- Open on iPhone
- Open on Android
- Test both light and dark mode

### Keep Test Campaign
- Don't delete test campaigns
- Reuse them for future tests
- Just update HTML each time
- Saves time recreating campaign

---

## 📞 Still Stuck?

**Braze Support:**
- Click ? icon in Braze dashboard
- Live chat available
- Email: support@braze.com

**Check This:**
- Are you on the right Braze workspace?
- Do you have email sending permissions?
- Is your account email verified?

---

## ✉️ What You'll Receive

When test email arrives, you'll see:

**Subject:** Test - Hero Variants

**From:** Tubi <hello@tubitv.com>

**Content:**
- 4 different hero variants
- Dual CTA buttons
- All styling from CSS block
- Images from placeholder URLs

**Check:**
- ✅ Images load
- ✅ Buttons are clickable
- ✅ Layout looks correct
- ✅ Dual CTAs side-by-side (desktop)
- ✅ Mobile: buttons stack

---

**Last Updated:** March 23, 2026
**Questions?** Check the other guides in this folder!
