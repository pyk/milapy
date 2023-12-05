import type { HeadConfig } from "vitepress";

const head: HeadConfig[] = [
  ["meta", { name: "theme-color", content: "#06b6d4" }],
  [
    "meta",
    { name: "viewport", content: "width=device-width, initial-scale=1.0" },
  ],
  ["meta", { name: "author", content: "sepyke" }],
  ["meta", { name: "referrer", content: "no-referrer-when-downgrade" }],

  ["link", { rel: "icon", type: "image/png", href: "/favicon.png" }],
  ["link", { rel: "apple-touch-icon", href: "/apple-touch-icon.png" }],
  ["link", { rel: "sitemap", href: "/sitemap.xml" }],
  ["meta", { name: "robots", content: "index, follow" }],

  ["meta", { name: "twitter:card", content: "summary_large_image" }],
  ["meta", { name: "twitter:site", content: "@sepyke" }],
  ["meta", { name: "twitter:creator", content: "@sepyke" }],

  ["meta", { property: "og:site_name", content: "milapy Documentation" }],
  ["meta", { property: "og:locale", content: "en_US" }],
];

export default head;
