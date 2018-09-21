<template>
  <div id="app">
    <div class="liubai"></div>
    <div class="logo">
      <div class="log"></div>
    </div>
    <div class="font">
      <p>人体姿态校准</p>
    </div>
    <div class="bt">
      <form @submit.prevent="upload" method="post" enctype="multipart/form-data">
        <div class="sub">
          <a href="javascript:;" class="file border-ra"><span class="bt-p">{{morename}}</span>
            <input type="file" name="more" v-on:change="onChangemore($event)">
          </a><br>
          <a href="javascript:;" class="file border-right"><span class="bt-p">{{filename}}</span>
            <input type="file" name="file" v-on:change="onChangeflie($event)">
          </a>
        </div>
        <p class="p1">有什么不了解？</p>
        <div class="bt1-wrapper">
          <button type="submit" class="bt1">上传图片</button>
        </div>
      </form>
    </div>
    <div class="font-wrapper">
      <a href="/#/video" class="goto">视频校准</a>
      <p class="p2">Want to know more about it?</p>
      <p class="p3">关于我们</p>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import { Toast, Dialog } from 'vant'

export default {
  name: 'App',
  data () {
    return {
      picture: {},
      filename: '图片二',
      morename: '图片一',
      file: {},
      more: {},
      result: ''
    }
  },
  methods: {
    onChangeflie: function (event) {
      this.file = event.target.files[0] // get input file object
      this.filename = this.file.name
      console.log(this.morename.length)
    },
    onChangemore: function (event) {
      this.more = event.target.files[0] // get input file object
      this.morename = this.more.name
      console.log(this.more)
    },
    upload: function () {
      if (this.filename === '图片二' || this.morename === '图片一') {
        Toast('请选图片')
        return
      }
      this.loding()
      var formData = new FormData()
      formData.append('file', this.file)
      formData.append('more', this.more)
      // specify Content-Type, with formData as well
      this.$http.post('http://127.0.0.1:8000/web/upload/getupload/', formData, {
        headers: {'Content-Type': 'multipart/form-data'}
      }).then((res) => {
        res = res.body
        this.result = res
        console.log(res)
        Dialog.alert({
          message: this.result
        }).then(() => {
          // on close
          Dialog.alert({
            message: this.result
          })
        })
      }, function (res) {
        console.log(res.body)
      })
    },
    loding () {
      Toast.loading({
        duration: 0, //  持续展示 toast
        forbidClick: true, // 禁用背景点击
        loadingType: 'spinner',
        mask: true,
        message: '请稍等...'
      })
    },
    clearLoding () {
      Toast.clear()
    }
  },
  watch: {
    'result' () {
      this.clearLoding()
    }
  },
  created () {
    const toast = Toast.loading({
      duration: 0, // 持续展示 toast
      forbidClick: true, // 禁用背景点击
      loadingType: 'spinner',
      message: '加载中 1 秒'
    })

    let second = 1
    const timer = setInterval(() => {
      second--
      if (second) {
        toast.message = `加载中 ${second} 秒`
      } else {
        clearInterval(timer)
        Toast.clear()
      }
    }, 1000)
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "../assets/css/reset.css"
  #app
    position absolute
    top 0
    bottom 0
    right 0
    left 0
    background url("../../static/img/bg1.png")
    .liubai
      height 16.6667%
      width 100%
    .logo
      width 100%
      height 11.4%
      .log
        width 20.41%
        height 100%
        background url("../../static/img/log.png")
        background-size 100% auto
        margin 0 auto
    .font
      p
        font-size: 32px
        color: #FFFFFF
        text-align: center
        margin-top: 20px
        font-family:"宋体"
    .bt
      width: 50%;
      height: 17.857%;
      margin: 50px auto 20px auto;
      .sub
        height: 41.6666%;
        display: flex
        .file
          width: 45%;
          text-align: center;
          position: relative;
          display: inline-block;
          border: 1px solid #99D3F5;
          padding: 13px 4px;
          overflow: hidden;
          color: rgba(0, 0, 0, 0.9);
          text-decoration: none;
          text-indent: 0;
          height: 41.6666%;
          font-size:16px;
          background:#ffffff;
          margin-bottom: 40px;
          flex: 1;
          white-space:nowrap;
          overflow: hidden;
          font-family '宋体'
        input
          position: absolute;
          font-size: 100px;
          right: 0;
          top: 0;
          opacity: 0;
        .border-ra
          border-radius: 20px 5px 5px 20px;
          margin-right: 2px
        .border-right
          border-radius: 5px 20px 20px 5px;
      .p1
        text-align: center;
        color: #FFFFFF;
        font-size: 14px;
        font-weight: 100;
      .bt1-wrapper
        width 85%
        margin 0 auto
        .bt1
          width: 100%;
          margin 40px auto 10px auto
          text-align: center;
          position: relative;
          font-family '宋体'
          display: inline-block;
          border: 1.5px solid #FFFFFF;
          border-radius: 100px;
          padding: 13px 4px;
          overflow: hidden;
          color: rgba(255, 255, 255, 0.9);
          text-decoration: none;
          text-indent: 0;
          font-size:16px;
          background: rgba(255, 255, 255, 0);
          outline:none;
        .bt1:active {background: rgba(255, 255, 255, 0.2)}
    .font-wrapper
      margin-top: 24%;
      font-size 12px
      line-height 30px
      color #fff
      text-align center
      .goto
        display block
        width 50%
        height 35px
        margin 0 auto
        line-height 35px
        color #FFFFFF
      .p3
        color #ffd180
</style>
