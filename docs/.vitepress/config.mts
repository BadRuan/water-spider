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
          link: "/database/table/waterlevel"
        }
      ]
  },
  {
    text: "数据大屏", items: [
      {
        text: "DataEase环境部署", link: "/dataease/env"
      }
    ]
  },
  {
    text: "开发进展", link: "/story/index"
  }
]

export default defineConfig({
  title: "水位数据自动化",
  description: "水位站数据自动化提取分析",
  themeConfig: {
    nav: nav_tmp,
    sidebar: nav_tmp,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/BadRuan/water-info' }
    ],
    footer: {
      copyright: 'Copyright © 2024 RuanFumin'
    }
  }
})
