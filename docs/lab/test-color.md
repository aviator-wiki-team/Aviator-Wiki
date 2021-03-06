## Material color palette 颜色主题

### Primary colors 主色

点击按钮可更换主题的主色(默认Light Blue)

<div id="color-button">
<button class="button button-rounded button-small" data-md-color-primary="red">Red</button>
<button class="button button-rounded button-small" data-md-color-primary="pink">Pink</button>
<button class="button button-rounded button-small" data-md-color-primary="purple">Purple</button>
<button class="button button-rounded button-small" data-md-color-primary="deep-purple">Deep Purple</button>
<button class="button button-rounded button-small" data-md-color-primary="indigo">Indigo</button>
<button class="button button-rounded button-small" data-md-color-primary="blue">Blue</button>
<button class="button button-rounded button-small" data-md-color-primary="light-blue">Light Blue</button>
<button class="button button-rounded button-small" data-md-color-primary="cyan">Cyan</button>
<button class="button button-rounded button-small" data-md-color-primary="teal">Teal</button>
<button class="button button-rounded button-small" data-md-color-primary="green">Green</button>
<button class="button button-rounded button-small" data-md-color-primary="light-green">Light Green</button>
<button class="button button-rounded button-small" data-md-color-primary="lime">Lime</button>
<button class="button button-rounded button-small" data-md-color-primary="yellow">Yellow</button>
<button class="button button-rounded button-small" data-md-color-primary="amber">Amber</button>
<button class="button button-rounded button-small" data-md-color-primary="orange">Orange</button>
<button class="button button-rounded button-small" data-md-color-primary="deep-orange">Deep Orange</button>
<button class="button button-rounded button-small" data-md-color-primary="brown">Brown</button>
<button class="button button-rounded button-small" data-md-color-primary="grey">Grey</button>
<button class="button button-rounded button-small" data-md-color-primary="blue-grey">Blue Grey</button>
<button class="button button-rounded button-small" data-md-color-primary="white">White</button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorPrimary = this.dataset.mdColorPrimary;
      localStorage.setItem("data-md-color-primary",this.dataset.mdColorPrimary);
    })
  })
</script>

### Accent colors 辅助色

点击按钮更换主题的辅助色（默认Red）

<div id="color-button">
<button class="button button-rounded button-small" data-md-color-accent="red">Red</button>
<button class="button button-rounded button-small" data-md-color-accent="pink">Pink</button>
<button class="button button-rounded button-small" data-md-color-accent="purple">Purple</button>
<button class="button button-rounded button-small" data-md-color-accent="deep-purple">Deep Purple</button>
<button class="button button-rounded button-small" data-md-color-accent="indigo">Indigo</button>
<button class="button button-rounded button-small" data-md-color-accent="blue">Blue</button>
<button class="button button-rounded button-small" data-md-color-accent="light-blue">Light Blue</button>
<button class="button button-rounded button-small" data-md-color-accent="cyan">Cyan</button>
<button class="button button-rounded button-small" data-md-color-accent="teal">Teal</button>
<button class="button button-rounded button-small" data-md-color-accent="green">Green</button>
<button class="button button-rounded button-small" data-md-color-accent="light-green">Light Green</button>
<button class="button button-rounded button-small" data-md-color-accent="lime">Lime</button>
<button class="button button-rounded button-small" data-md-color-accent="yellow">Yellow</button>
<button class="button button-rounded button-small" data-md-color-accent="amber">Amber</button>
<button class="button button-rounded button-small" data-md-color-accent="orange">Orange</button>
<button class="button button-rounded button-small" data-md-color-accent="deep-orange">Deep Orange</button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorAccent = this.dataset.mdColorAccent;
      localStorage.setItem("data-md-color-accent",this.dataset.mdColorAccent);
    })
  })

  // #758
  document.getElementsByClassName('md-nav__title')[1].click()
</script>

### Thanks:

- [OI-WIki](https://oi-wiki.org) 借鉴了该项目的Extra.js
- [Buttons.css](https://unicorn-ui.com/buttons/) Button.css 样式供应商
