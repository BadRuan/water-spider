import { defineConfig } from 'vitepress'

let nav_tmp = [
  { text: '首页', link: '/' },
  {
    text: '数据库', items:
      [
        {
          text: "搭建数据库",
          link: "/database/setenv"
        },
        {
          text: "水位信息数据表",
          link: "/database/waterlevel"
        }
      ]
  },
  {
    text: "开发进展", link: "/story/index"
  }
]

export default defineConfig({
  title: "水位数据爬虫",
  description: "安徽水文站水位数据自动化提取",
  themeConfig: {
    nav: nav_tmp,
    sidebar: nav_tmp,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/BadRuan/water-spider' }
    ],
    footer: {
      copyright: 'Copyright © 2024 RuanFumin'
    }
  }
})
