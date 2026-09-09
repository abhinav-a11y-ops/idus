# Google Analytics Setup Guide for IDUS Website

## 📊 Google Analytics Integration

Google Analytics has been added to your IDUS website. Follow these steps to activate tracking:

---

## Step 1: Create Google Analytics Account

1. Go to: https://analytics.google.com/
2. Click **Start measuring**
3. Enter your account name: `IDUS Platform`
4. Click **Next**

---

## Step 2: Create Property

1. **Property name:** `IDUS Website`
2. **Reporting timezone:** Select your timezone
3. **Currency:** INR (Indian Rupee)
4. Click **Next**

---

## Step 3: Create Data Stream

1. **Platform:** Select **Web**
2. **Website URL:** `https://abhinav-a11y-ops.github.io/idus-deployment-website/`
3. **Stream name:** `IDUS GitHub Pages`
4. Click **Create stream**

---

## Step 4: Get Your Measurement ID

After creating the stream, you'll see:
- **Measurement ID:** `G-XXXXXXXXXX` (format: G- followed by 10 characters)

---

## Step 5: Update Website Code

Replace `G-XXXXXXXXXX` in the HTML file with your actual Measurement ID:

**Near the end of `index.html`'s body, in the consent/analytics script — there is exactly one value to change (`MEASUREMENT_ID`):**

```html
<!-- Before -->
var MEASUREMENT_ID = 'G-XXXXXXXXXX';
```

**After (example):**
```html
<!-- After -->
var MEASUREMENT_ID = 'G-ABC123DEF4';
```

> **Note on consent:** the analytics tag loads *only after* a visitor clicks
> “Allow analytics” in the consent banner (or returns after allowing it).
> Until then no tag, no cookies. Once consent is given, the tag loads
> dynamically from `www.googletagmanager.com` and `gtag('config', …)` runs
> automatically — no further code changes are needed.

---

## Step 6: Deploy Updated Code

1. Update the HTML file with your Measurement ID
2. Commit and push to GitHub:
   ```bash
   git add index.html
   git commit -m "Add Google Analytics tracking ID"
   git push origin master
   ```
3. GitHub Pages will auto-deploy (2-3 minutes)

---

## Step 7: Verify Analytics

1. Go back to Google Analytics
2. Click **Admin** (bottom left)
3. Go to **Data Streams**
4. Click your stream
5. Scroll to **Tagging instructions** → **Install tag manually**
6. Check the status - it should show "Collecting data" after a few minutes

---

## 📈 What You'll Track

Once activated, Google Analytics will track:

✅ **Page Views** - How many people visit your site
✅ **Sessions** - How long users stay on your site
✅ **Users** - Unique visitor count
✅ **Bounce Rate** - % of users who leave without interaction
✅ **Traffic Source** - Where visitors come from (Google, social, direct)
✅ **Device Info** - Mobile, tablet, desktop breakdown
✅ **Geographic Data** - Visitor locations
✅ **Referrals** - Which sites link to you
✅ **Events** - Button clicks, link clicks, form submissions

---

## 🎯 Key Analytics Dashboards

### Real-time Dashboard
- **Path:** Analytics → Real-time
- **Shows:** Live visitor activity

### Audience Overview
- **Path:** Analytics → Audience → Overview
- **Shows:** Total users, sessions, bounce rate

### Acquisition Report
- **Path:** Analytics → Acquisition → Traffic source
- **Shows:** Where traffic comes from

### Pages Report
- **Path:** Analytics → Engagement → Pages and screens
- **Shows:** Most visited pages

---

## 🔧 Advanced Setup (Optional)

### Track Button Clicks
Add to any button:
```html
<button onclick="gtag('event', 'button_click', {'button_name': 'Start Free Trial'})">
    Start Free Trial
</button>
```

### Track External Links
```html
<a href="https://serene-idus-a35dd0.netlify.app" 
   onclick="gtag('event', 'external_link', {'url': this.href})">
    Launch IDUS Platform
</a>
```

### Track Form Submissions
```html
<form onsubmit="gtag('event', 'form_submit', {'form_name': 'contact'})">
    <!-- form fields -->
</form>
```

---

## 📱 Mobile App Tracking (Optional)

If you want to track the IDUS platform app separately:
1. Create another property in Google Analytics
2. Select **Mobile app** as platform
3. Get a different Measurement ID
4. Add it to your IDUS platform code

---

## 🔐 Privacy & GDPR

**Important:** If you have users from EU:
1. Add a cookie consent banner
2. Update Privacy Policy
3. Configure Google Analytics for GDPR compliance

---

## 📞 Support

- **Google Analytics Help:** https://support.google.com/analytics
- **Measurement ID Format:** Always starts with `G-`
- **Setup Time:** Usually takes 24-48 hours to see data

---

## ✅ Checklist

- [ ] Created Google Analytics account
- [ ] Created property for IDUS Website
- [ ] Created web data stream
- [ ] Got Measurement ID (G-XXXXXXXXXX)
- [ ] Updated index.html with your ID
- [ ] Committed and pushed to GitHub
- [ ] Verified "Collecting data" status
- [ ] Checked Real-time dashboard for visitors

Your Google Analytics is now tracking IDUS website visitors! 📊
