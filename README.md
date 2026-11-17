# Hulul Group · مجموعة حلول

<p dir="rtl" lang="ar">تقدّم مجموعة حلول خدمات التسويق الرقمي وتصميم الهويّات وتطوير المواقع والمتاجر الإلكترونية والبرمجيات وأتمتة واتساب. يعمل فريقنا من بغداد مع شركات في الشرق الأوسط وشمال أفريقيا.</p>

<p dir="rtl" lang="ar"><a href="https://hulul.group/ar">الموقع الرسمي بالعربية</a> · <a href="https://hulul.group/ar/work">المشاريع المنشورة</a></p>

Hulul Group provides digital marketing, brand design, websites, e-commerce, custom software and WhatsApp automation. Our team works from Baghdad with companies across the Middle East and North Africa.

[Official website in English](https://hulul.group/en) · [Selected work](https://hulul.group/en/work)

## فحص موقع بالعربية والإنجليزية قبل الإطلاق

<p dir="rtl" lang="ar">قد تعمل الصفحة بالعربية والإنجليزية في المتصفّح، بينما يشير رمز اللغة أو العنوان الأساسي في ملف الصفحة إلى النسخة الخطأ. تفحص هذه الأداة النسختين من الاستجابة الأولى، وتبيّن إن كان اتجاه القراءة صحيحاً، والعنوان الأساسي مطابقاً، وروابط <code>hreflang</code> متبادلة. جرّبها على صفحة واحدة قبل اعتماد بقية الصفحات.</p>

## Check an Arabic–English page pair before release

Pass the two canonical URLs for equivalent pages to [the Python checker](check-language-pair.py). It checks the initial HTML and HTTP headers for a direct HTTP 200, the expected language and reading direction, one self-referencing canonical, and reciprocal `hreflang="ar"` and `hreflang="en"` links. Use `--default` when you want to verify an `x-default` target. The checker exits with status 1 if a check fails.

```sh
python3 check-language-pair.py \
  https://hulul.group/ar/brand/site \
  https://hulul.group/en/brand/site \
  --default https://hulul.group/en/brand/site
```

<p dir="rtl" lang="ar">بعد نجاح الفحص، جرّب بنفسك تبديل اللغة على الهاتف وإرسال استفسار. ثم استخدم Search Console لمراجعة ما يراه Google بعد الزحف. يشرح دليلنا العملي كيف يختبر فريقك هذه الخطوات عند استلام الموقع.</p>

Continue with the mobile language switch and enquiry tests in our handover guide. Use Search Console to check Google’s crawl and indexing status.

[دليل استلام موقع شركة بالعربية والإنجليزية](https://hulul.group/ar/blog/bilingual-company-website-checklist) · [English handover guide](https://hulul.group/en/blog/bilingual-company-website-checklist)

[Google’s localized-page guidance](https://developers.google.com/search/docs/specialty/international/localized-versions) · [Google’s canonical URL guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [OpenSEO project](https://github.com/every-app/open-seo)
