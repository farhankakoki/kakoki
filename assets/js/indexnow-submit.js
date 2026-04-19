<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>IndexNow Submission — KAKOKI Creative Co.</title>
  <style>
    body { font-family: monospace; background: #111; color: #0f0; padding: 2rem; line-height: 2; }
    button { background: #1D9E75; color: #fff; border: none; padding: 12px 28px; font-size: 16px; cursor: pointer; border-radius: 4px; font-family: monospace; }
    button:hover { background: #17856a; }
    #log { margin-top: 1.5rem; background: #000; padding: 1rem; min-height: 200px; white-space: pre-wrap; overflow-y: auto; max-height: 500px; border: 1px solid #333; }
    .ok { color: #0f0; }
    .err { color: #f55; }
    .info { color: #09f; }
  </style>
</head>
<body>
  <h1 style="color:#fff;font-size:1.4rem;margin-bottom:1rem;">⚡ KAKOKI IndexNow — Instant Indexing Submission</h1>
  <p style="color:#888;margin-bottom:1.5rem;font-size:0.85rem;">
    Pings Google, Bing &amp; Yandex simultaneously via IndexNow API.<br>
    Run once after deploying any site changes. Check DevTools Console for responses.
  </p>

  <button onclick="submitIndexNow()">▶ Submit All 15 URLs to IndexNow</button>
  <div id="log"><span class="info">Ready. Click button to submit.</span></div>

  <script>
    const KEY = "ad8e553c327f459b8695a2b6e2825c86";
    const HOST = "kakokicreative.in";

    const URLS = [
      "https://kakokicreative.in/",
      "https://kakokicreative.in/areekode/",
      "https://kakokicreative.in/blog/",
      "https://kakokicreative.in/branding-areekode/",
      "https://kakokicreative.in/contact/",
      "https://kakokicreative.in/creative-agency-kerala/",
      "https://kakokicreative.in/farhan-mubeen/",
      "https://kakokicreative.in/gulf-nri-web-design/",
      "https://kakokicreative.in/service-areas-malappuram/",
      "https://kakokicreative.in/web-design-kozhikode/",
      "https://kakokicreative.in/web-design-malappuram/",
      "https://kakokicreative.in/web-design-manjeri/",
      "https://kakokicreative.in/web-design-perinthalmanna/",
      "https://kakokicreative.in/web-design-tirur/",
      "https://kakokicreative.in/blog/why-every-business-in-malappuram-needs-a-professional-website-2026/"
    ];

    const ENDPOINTS = [
      "https://api.indexnow.org/indexnow",
      "https://www.bing.com/indexnow",
      "https://yandex.com/indexnow"
    ];

    const log = document.getElementById("log");
    function write(msg, cls = "") {
      const span = document.createElement("span");
      span.className = cls;
      span.textContent = msg + "\n";
      log.appendChild(span);
      log.scrollTop = log.scrollHeight;
    }

    async function submitIndexNow() {
      log.innerHTML = "";
      write(`[${new Date().toISOString()}] Starting IndexNow submission...`, "info");
      write(`URLs to submit: ${URLS.length}`, "info");
      write("", "");

      const payload = {
        host: HOST,
        key: KEY,
        keyLocation: `https://${HOST}/${KEY}.txt`,
        urlList: URLS
      };

      for (const endpoint of ENDPOINTS) {
        write(`→ Submitting to: ${endpoint}`, "info");
        try {
          const res = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json; charset=utf-8" },
            body: JSON.stringify(payload)
          });
          if (res.ok || res.status === 200 || res.status === 202) {
            write(`  ✓ SUCCESS [HTTP ${res.status}] — ${endpoint}`, "ok");
          } else {
            write(`  ✗ HTTP ${res.status} — ${endpoint}`, "err");
          }
        } catch (err) {
          write(`  ✗ ERROR — ${endpoint}: ${err.message}`, "err");
          write(`  (CORS may block browser fetch; use server-side submission for Yandex)`, "err");
        }
        write("", "");
      }

      write("─────────────────────────────────────", "info");
      write("Submission complete. URLs submitted:", "info");
      URLS.forEach((u, i) => write(`  ${i + 1}. ${u}`, "ok"));
      write("", "");
      write("Next steps:", "info");
      write("  1. Go to Google Search Console → URL Inspection → request indexing for each URL", "info");
      write("  2. Submit sitemap: https://kakokicreative.in/sitemap.xml", "info");
      write("  3. Check GSC Coverage report in 7 days", "info");
    }
  </script>
</body>
</html>
