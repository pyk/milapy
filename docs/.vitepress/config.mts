import { defineConfig } from "vitepress";

import head from "./head";
import generateDynamicMeta from "./generateDynamicMeta";

const hostname: string = "https://milapy.dev";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Milapy Documentation",
  titleTemplate: ":title — Milapy Documentation",
  description:
    "Simple & extensible Python 3 interface designed for Ethereum and various EVM-based chains",
  head: head,
  transformHead(context) {
    return generateDynamicMeta(context, hostname);
  },
  lastUpdated: true,
  cleanUrls: true,
  lang: "en-US",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    siteTitle: "milapy",
    socialLinks: [
      { icon: "github", link: "https://github.com/pyk/milapy" },
      { icon: "twitter", link: "https://x.com/sepyke" },
    ],

    sidebar: [
      {
        text: "Getting started",
        link: "/",
      },
    ],
    search: {
      provider: "local",
      options: {
        detailedView: true,
      },
    },
  },
  sitemap: {
    hostname: "https://milapy.dev",
  },
});
