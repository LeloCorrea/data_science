(window["webpackJsonpstreamlit-browser"]=window["webpackJsonpstreamlit-browser"]||[]).push([[17],{1042:function(e,t,r){"use strict";var n=r(0),o=r(154),i=r(1059);function a(){return(a=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function c(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var r=[],n=!0,o=!1,i=void 0;try{for(var a,c=e[Symbol.iterator]();!(n=(a=c.next()).done)&&(r.push(a.value),!t||r.length!==t);n=!0);}catch(u){o=!0,i=u}finally{try{n||null==c.return||c.return()}finally{if(o)throw i}}return r}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function u(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}t.a=n.forwardRef(function(e,t){var r=e.children,s=e.title,l=e.overrides,p=void 0===l?{}:l,f=e.size,d=e.color,y=u(e,["children","title","overrides","size","color"]),b=c(Object(o.c)(p.Svg,i.a),2),g=b[0],m=b[1],v={$size:f,$color:d};return n.createElement(g,a({"data-baseweb":"icon",ref:t},y,v,m),s?n.createElement("title",null,s):null,r)})},1053:function(e,t,r){"use strict";function n(e){var t={};for(var r in e)"$"!==r[0]&&(t[r]=e[r]);return t}r.d(t,"a",function(){return n})},1059:function(e,t,r){"use strict";r.d(t,"b",function(){return o}),r.d(t,"a",function(){return i});var n=r(401);function o(e){var t=e.$theme,r=e.$size,n=e.$color;return r?t.sizing[r]?r=t.sizing[r]:"number"===typeof r&&(r="".concat(r,"px")):r=t.sizing.scale600,n&&t.colors[n]&&(n=t.colors[n]),{display:"inline-block",fill:n||"currentColor",color:n||"currentColor",height:r,width:r}}var i=Object(n.a)("svg",o);i.displayName="Svg"},1076:function(e,t,r){"use strict";r.d(t,"b",function(){return n}),r.d(t,"a",function(){return o}),r.d(t,"d",function(){return i}),r.d(t,"c",function(){return a});var n={textarea:"textarea"},o={none:"none",left:"left",right:"right",both:"both"},i={mini:"mini",default:"default",compact:"compact",large:"large"},a={start:"start",end:"end"}},1132:function(e,t,r){var n;!function(){"use strict";var o={not_string:/[^s]/,not_bool:/[^t]/,not_type:/[^T]/,not_primitive:/[^v]/,number:/[diefg]/,numeric_arg:/[bcdiefguxX]/,json:/[j]/,not_json:/[^j]/,text:/^[^\x25]+/,modulo:/^\x25{2}/,placeholder:/^\x25(?:([1-9]\d*)\$|\(([^)]+)\))?(\+)?(0|'[^$])?(-)?(\d+)?(?:\.(\d+))?([b-gijostTuvxX])/,key:/^([a-z_][a-z_\d]*)/i,key_access:/^\.([a-z_][a-z_\d]*)/i,index_access:/^\[(\d+)\]/,sign:/^[+-]/};function i(e){return function(e,t){var r,n,a,c,u,s,l,p,f,d=1,y=e.length,b="";for(n=0;n<y;n++)if("string"===typeof e[n])b+=e[n];else if("object"===typeof e[n]){if((c=e[n]).keys)for(r=t[d],a=0;a<c.keys.length;a++){if(void 0==r)throw new Error(i('[sprintf] Cannot access property "%s" of undefined value "%s"',c.keys[a],c.keys[a-1]));r=r[c.keys[a]]}else r=c.param_no?t[c.param_no]:t[d++];if(o.not_type.test(c.type)&&o.not_primitive.test(c.type)&&r instanceof Function&&(r=r()),o.numeric_arg.test(c.type)&&"number"!==typeof r&&isNaN(r))throw new TypeError(i("[sprintf] expecting number but found %T",r));switch(o.number.test(c.type)&&(p=r>=0),c.type){case"b":r=parseInt(r,10).toString(2);break;case"c":r=String.fromCharCode(parseInt(r,10));break;case"d":case"i":r=parseInt(r,10);break;case"j":r=JSON.stringify(r,null,c.width?parseInt(c.width):0);break;case"e":r=c.precision?parseFloat(r).toExponential(c.precision):parseFloat(r).toExponential();break;case"f":r=c.precision?parseFloat(r).toFixed(c.precision):parseFloat(r);break;case"g":r=c.precision?String(Number(r.toPrecision(c.precision))):parseFloat(r);break;case"o":r=(parseInt(r,10)>>>0).toString(8);break;case"s":r=String(r),r=c.precision?r.substring(0,c.precision):r;break;case"t":r=String(!!r),r=c.precision?r.substring(0,c.precision):r;break;case"T":r=Object.prototype.toString.call(r).slice(8,-1).toLowerCase(),r=c.precision?r.substring(0,c.precision):r;break;case"u":r=parseInt(r,10)>>>0;break;case"v":r=r.valueOf(),r=c.precision?r.substring(0,c.precision):r;break;case"x":r=(parseInt(r,10)>>>0).toString(16);break;case"X":r=(parseInt(r,10)>>>0).toString(16).toUpperCase()}o.json.test(c.type)?b+=r:(!o.number.test(c.type)||p&&!c.sign?f="":(f=p?"+":"-",r=r.toString().replace(o.sign,"")),s=c.pad_char?"0"===c.pad_char?"0":c.pad_char.charAt(1):" ",l=c.width-(f+r).length,u=c.width&&l>0?s.repeat(l):"",b+=c.align?f+r+u:"0"===s?f+u+r:u+f+r)}return b}(function(e){if(c[e])return c[e];var t,r=e,n=[],i=0;for(;r;){if(null!==(t=o.text.exec(r)))n.push(t[0]);else if(null!==(t=o.modulo.exec(r)))n.push("%");else{if(null===(t=o.placeholder.exec(r)))throw new SyntaxError("[sprintf] unexpected placeholder");if(t[2]){i|=1;var a=[],u=t[2],s=[];if(null===(s=o.key.exec(u)))throw new SyntaxError("[sprintf] failed to parse named argument key");for(a.push(s[1]);""!==(u=u.substring(s[0].length));)if(null!==(s=o.key_access.exec(u)))a.push(s[1]);else{if(null===(s=o.index_access.exec(u)))throw new SyntaxError("[sprintf] failed to parse named argument key");a.push(s[1])}t[2]=a}else i|=2;if(3===i)throw new Error("[sprintf] mixing positional and named placeholders is not (yet) supported");n.push({placeholder:t[0],param_no:t[1],keys:t[2],sign:t[3],pad_char:t[4],align:t[5],width:t[6],precision:t[7],type:t[8]})}r=r.substring(t[0].length)}return c[e]=n}(e),arguments)}function a(e,t){return i.apply(null,[e].concat(t||[]))}var c=Object.create(null);t.sprintf=i,t.vsprintf=a,"undefined"!==typeof window&&(window.sprintf=i,window.vsprintf=a,void 0===(n=function(){return{sprintf:i,vsprintf:a}}.call(t,r,t,e))||(e.exports=n))}()},1166:function(e,t,r){"use strict";var n=r(0),o=r(401),i=r(154),a=r(1042),c=r(1053);function u(){return(u=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function s(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),r.push.apply(r,n)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?s(Object(r),!0).forEach(function(t){p(e,t,r[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))})}return e}function p(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function f(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}function d(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var r=[],n=!0,o=!1,i=void 0;try{for(var a,c=e[Symbol.iterator]();!(n=(a=c.next()).done)&&(r.push(a.value),!t||r.length!==t);n=!0);}catch(u){o=!0,i=u}finally{try{n||null==c.return||c.return()}finally{if(o)throw i}}return r}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}t.a=n.forwardRef(function(e,t){var r=d(Object(o.b)(),2)[1],s=e.overrides,p=void 0===s?{}:s,y=f(e,["overrides"]),b=Object(i.d)({component:r.icons&&r.icons.DeleteAlt?r.icons.DeleteAlt:null,props:l({title:"Delete Alt",viewBox:"0 0 24 24"},Object(c.a)(y))},p&&p.Svg?Object(i.f)(p.Svg):{});return n.createElement(a.a,u({title:"Delete Alt",viewBox:"0 0 24 24",ref:t,overrides:{Svg:b}},y),n.createElement("path",{fillRule:"evenodd",clipRule:"evenodd",d:"M12 20C16.4183 20 20 16.4183 20 12C20 7.58173 16.4183 4 12 4C7.58173 4 4 7.58173 4 12C4 16.4183 7.58173 20 12 20ZM10.0303 8.96967C9.73743 8.67679 9.26257 8.67679 8.96967 8.96967C8.67676 9.26257 8.67676 9.73743 8.96967 10.0303L10.9393 12L8.96967 13.9697C8.67676 14.2626 8.67676 14.7374 8.96967 15.0303C9.26257 15.3232 9.73743 15.3232 10.0303 15.0303L12 13.0607L13.9697 15.0303C14.2626 15.3232 14.7374 15.3232 15.0303 15.0303C15.3232 14.7374 15.3232 14.2626 15.0303 13.9697L13.0607 12L15.0303 10.0303C15.3232 9.73743 15.3232 9.26257 15.0303 8.96967C14.7374 8.67679 14.2626 8.67679 13.9697 8.96967L12 10.9393L10.0303 8.96967Z"}))})},1329:function(e,t,r){"use strict";var n=r(0),o=r(154),i=r(1227),a=r(1341),c=r(1126),u=r(1076);function s(e){return(s="function"===typeof Symbol&&"symbol"===typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"===typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function l(){return(l=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function p(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var r=[],n=!0,o=!1,i=void 0;try{for(var a,c=e[Symbol.iterator]();!(n=(a=c.next()).done)&&(r.push(a.value),!t||r.length!==t);n=!0);}catch(u){o=!0,i=u}finally{try{n||null==c.return||c.return()}finally{if(o)throw i}}return r}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function f(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}function d(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function y(e){return(y=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function b(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function g(e,t){return(g=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function m(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var v=function(e){function t(){var e,r,n,o;!function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,t);for(var i=arguments.length,a=new Array(i),c=0;c<i;c++)a[c]=arguments[c];return n=this,o=(e=y(t)).call.apply(e,[this].concat(a)),r=!o||"object"!==s(o)&&"function"!==typeof o?b(n):o,m(b(r),"state",{isFocused:r.props.autoFocus||!1}),m(b(r),"onFocus",function(e){r.setState({isFocused:!0}),r.props.onFocus(e)}),m(b(r),"onBlur",function(e){r.setState({isFocused:!1}),r.props.onBlur(e)}),r}var r,v,w;return function(e,t){if("function"!==typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&g(e,t)}(t,n["Component"]),r=t,(v=[{key:"render",value:function(){var e=this.props,t=e.startEnhancer,r=e.endEnhancer,s=e.overrides,d=s.Root,y=s.StartEnhancer,b=s.EndEnhancer,g=f(s,["Root","StartEnhancer","EndEnhancer"]),m=f(e,["startEnhancer","endEnhancer","overrides"]),v=p(Object(o.c)(d,c.d),2),w=v[0],O=v[1],j=p(Object(o.c)(y,c.c),2),S=j[0],E=j[1],x=p(Object(o.c)(b,c.c),2),k=x[0],_=x[1],P=Object(i.a)(this.props,this.state);return n.createElement(w,l({"data-baseweb":"input"},P,O),t&&n.createElement(S,l({},P,E,{$position:u.c.start}),"function"===typeof t?t(P):t),n.createElement(a.a,l({},m,{overrides:g,adjoined:h(t,r),onFocus:this.onFocus,onBlur:this.onBlur})),r&&n.createElement(k,l({},P,_,{$position:u.c.end}),"function"===typeof r?r(P):r))}}])&&d(r.prototype,v),w&&d(r,w),t}();function h(e,t){return e&&t?u.a.both:e?u.a.left:t?u.a.right:u.a.none}m(v,"defaultProps",{autoComplete:"on",autoFocus:!1,disabled:!1,name:"",error:!1,onBlur:function(){},onFocus:function(){},overrides:{},required:!1,size:u.d.default,startEnhancer:null,endEnhancer:null}),t.a=v},2339:function(e,t,r){},2387:function(e,t,r){"use strict";r.r(t);var n=r(6),o=r(11),i=r(14),a=r(12),c=r(13),u=r(20),s=r(0),l=r.n(s),p=r(1132),f=r(1329),d=r(17),y=r(62),b=(r(2339),function(e){function t(e){var r;Object(n.a)(this,t),(r=Object(i.a)(this,Object(a.a)(t).call(this,e))).inputRef=l.a.createRef(),r.formatValue=function(e){var t=r.props.element.get("format");if(null==t)return String(e);try{return Object(p.sprintf)(t,e)}catch(n){return Object(d.d)("Error in sprintf(".concat(t,", ").concat(e,"): ").concat(n)),String(e)}},r.isIntData=function(){return r.props.element.get("dataType")===u.j.DataType.INT},r.getMin=function(){return r.props.element.get("hasMin")?r.props.element.get("min"):-1/0},r.getMax=function(){return r.props.element.get("hasMax")?r.props.element.get("max"):1/0},r.getStep=function(){var e=r.props.element.get("step");return e||(r.isIntData()?1:.01)},r.setWidgetValue=function(e){var t=r.state.value,n=r.props,o=n.element,i=n.widgetMgr,a=r.props.element,c=o.get("id"),u=r.getMin(),s=r.getMax();if(u>t||t>s){var l=r.inputRef.current;l&&l.reportValidity()}else{var p=t||0===t?t:a.get("default");r.isIntData()?i.setIntValue(c,p,e):i.setFloatValue(c,p,e),r.setState({dirty:!1,value:p,formattedValue:r.formatValue(p)})}},r.onBlur=function(){r.state.dirty&&r.setWidgetValue({fromUi:!0})},r.onChange=function(e){var t=e.target.value,n=null;n=r.isIntData()?parseInt(t):parseFloat(t),r.setState({dirty:!0,value:n,formattedValue:t})},r.onKeyDown=function(e){switch(e.key){case"ArrowUp":e.preventDefault(),r.modifyValueUsingStep("increment")();break;case"ArrowDown":e.preventDefault(),r.modifyValueUsingStep("decrement")()}},r.onKeyPress=function(e){"Enter"===e.key&&r.state.dirty&&r.setWidgetValue({fromUi:!0})},r.modifyValueUsingStep=function(e){return function(){var t=r.state.value,n=r.getStep(),o=r.getMin(),i=r.getMax();switch(e){case"increment":t+n<=i&&r.setState({dirty:!0,value:t+n},function(){r.setWidgetValue({fromUi:!0})});break;case"decrement":t-n>=o&&r.setState({dirty:!0,value:t-n},function(){r.setWidgetValue({fromUi:!0})})}}},r.render=function(){var e=r.props,t=e.element,n=e.width,o=e.disabled,i=r.state,a=i.formattedValue,c=i.dirty,u=t.get("label"),s={width:n};return l.a.createElement("div",{className:"Widget row-widget stNumberInput",style:s},l.a.createElement("label",null,u),l.a.createElement("div",{className:"input-container"},l.a.createElement(f.a,{type:"number",inputRef:r.inputRef,value:a,onBlur:r.onBlur,onChange:r.onChange,onKeyPress:r.onKeyPress,onKeyDown:r.onKeyDown,disabled:o,overrides:{Input:{props:{step:r.getStep(),min:r.getMin(),max:r.getMax()}},InputContainer:{style:function(){return{borderTopRightRadius:0,borderBottomRightRadius:0}}}}}),l.a.createElement("div",{className:"controls"},l.a.createElement("button",{className:"control step-down",onClick:r.modifyValueUsingStep("decrement")},l.a.createElement(y.a,{type:"minus"})),l.a.createElement("button",{className:"control step-up",onClick:r.modifyValueUsingStep("increment")},l.a.createElement(y.a,{type:"plus"})))),c&&l.a.createElement("div",{className:"instructions"},"Press Enter to apply"))};var o=r.props.element.get("default");return r.state={dirty:!1,value:o,formattedValue:r.formatValue(o)},r}return Object(c.a)(t,e),Object(o.a)(t,[{key:"componentDidMount",value:function(){this.setWidgetValue({fromUi:!1})}}]),t}(l.a.PureComponent));r.d(t,"default",function(){return b})}}]);
//# sourceMappingURL=17.34258d6b.chunk.js.map