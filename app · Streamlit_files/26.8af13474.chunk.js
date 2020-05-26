(window["webpackJsonpstreamlit-browser"]=window["webpackJsonpstreamlit-browser"]||[]).push([[26],{1612:function(e,t,r){},2365:function(e,t,r){"use strict";r.r(t);var n,o=r(36),a=r(6),i=r(11),c=r(14),s=r(12),l=r(121),u=r(13),d=r(0),h=r.n(d),m=r(220);!function(e){e.ASCENDING="ascending",e.DESCENDING="descending"}(n||(n={}));var f=r(62);var b=function(e){function t(){return Object(a.a)(this,t),Object(c.a)(this,Object(s.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e,t,r,o=this.props,a=o.columnIndex,i=o.rowIndex,c=o.className,s=o.style,l=o.contents,u=o.columnSortDirection,d=o.headerClickedCallback,m=o.sortedByUser,b=l,p=u===n.DESCENDING;null!=d&&0===i&&(e=function(){return d(a)},t="button",r=0,b=null==u?'Sort by column "'.concat(l,'"'):'Sorted by column "'.concat(l,'" (').concat(p?"descending":"ascending",")"));var v=0===i?function(e){switch(e){case n.ASCENDING:return h.a.createElement(f.a,{className:"sort-arrow-icon",type:"chevron-top"});case n.DESCENDING:return h.a.createElement(f.a,{className:"sort-arrow-icon",type:"chevron-bottom"});case void 0:default:return null}}(u):void 0;return h.a.createElement("div",{className:c,style:s,onClick:e,role:t,tabIndex:r,title:b},m?v:"",l)}}]),t}(d.PureComponent),p=r(214),v=r(107),y=r(83);r(1612);function w(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),r.push.apply(r,n)}return r}var g=10,O=25,N=200,C=400,D=function(e){function t(e){var r;return Object(a.a)(this,t),(r=Object(c.a)(this,Object(s.a)(t).call(this,e))).multiGridRef=h.a.createRef(),r.state={sortedByUser:!1,sortColumn:0,sortDirection:n.ASCENDING},r.toggleSortOrder=r.toggleSortOrder.bind(Object(l.a)(r)),r}return Object(u.a)(t,e),Object(i.a)(t,[{key:"getCellRenderer",value:function(e){var t=this;return function(r){var n=r.columnIndex,a=r.key,i=r.rowIndex,c=r.style,s=e(n,i),l=s.classes,u=s.styles,d=s.contents,m=0===i?t.toggleSortOrder:void 0,f=n===t.state.sortColumn?t.state.sortDirection:void 0,p=function(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?w(r,!0).forEach(function(t){Object(o.a)(e,t,r[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):w(r).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))})}return e}({},c,{},u);return h.a.createElement(b,{key:a,columnIndex:n,rowIndex:i,className:l,style:p,contents:d,sortedByUser:t.state.sortedByUser,columnSortDirection:f,headerClickedCallback:m})}}},{key:"toggleSortOrder",value:function(e){var t=n.ASCENDING;this.state.sortColumn===e&&(t=this.state.sortDirection!==n.ASCENDING?n.ASCENDING:n.DESCENDING),this.setState({sortColumn:e,sortDirection:t,sortedByUser:!0})}},{key:"getDataRowIndices",value:function(){var e=this.props.element,t=this.state,r=t.sortColumn,o=t.sortDirection,a=Object(v.c)(e),i=a.headerCols,c=a.dataRows,s=o!==n.DESCENDING;if(r<i){for(var l=new Array(c),u=0;u<c;u+=1)l[u]=s?u:c-(u+1);return l}return Object(v.e)(e,r-i,s)}},{key:"getDimensions",value:function(e){var t=this.props,r=t.element,n=t.width,o=t.height,a=Object(v.c)(r),i=a.headerRows,c=a.headerCols,s=a.dataRows,l=a.cols,u=a.rows,d=25*i,h=function(e,t,r,n,o,a){var i=O,c=e>2?N:C,s=[],l=Array.from(Array(e),function(e,r){return function(e){for(var r=e.index,o=14+g,c=i,s=0;s<Math.min(t,100);s++){var l=-1;l=s<n?s:t>100?Math.floor(Math.random()*t):s;var u=a(r,l).contents,d=8*(u?u.length:0)+o;d>c&&(c=d)}return c}({index:r})}),u=l.reduce(function(e,t){return e+t},0),d=o-u;if(d<0)s=l.map(function(e){return e>c?c:e});else{var h=l.filter(function(e){return e>c}),m=d/h.length;s=l.map(function(e,t){return t in h.keys()?e+m:e})}var f=s.reduce(function(e,t){return e+t},0);if(f>o*(2/3)&&f<o){var b=(o-f)/e;s=s.map(function(e){return e+b}),f=s.reduce(function(e,t){return e+t},0)}var p=Math.min(f,o),v=s.slice(0,r).reduce(function(e,t){return e+t});return{elementWidth:p,columnWidth:function(e){var t=e.index;return s[t]},headerWidth:v}}(l,u,c,i,n-2,e),m=h.elementWidth,f=h.columnWidth,b=h.headerWidth;if(0===s&&m<60){m=60,b=60;for(var p=0,y=0;y<l;y++)p+=f({index:y});p<60&&(f=function(){return 60/l})}return{rowHeight:25,headerHeight:d,border:2,height:Math.min(25*u,o||300),elementWidth:m,columnWidth:f,headerWidth:b}}},{key:"recomputeSizeIfNeeded",value:function(){var e=this;setTimeout(function(){null!=e.multiGridRef.current&&e.multiGridRef.current.recomputeGridSize()},0)}},{key:"render",value:function(){var e=this.props.element,t=Object(v.c)(e),r=t.headerRows,n=t.headerCols,o=t.dataRows,a=t.cols,i=t.rows,c=function(e,t,r,n){return function(r,o){if(null!=n&&o>=t){var a=o-t;a>=0&&a<n.length?(o=n[a],o+=t):console.warn("Bad sortedDataRowIndices ("+"rowIndex=".concat(o,", ")+"headerRows=".concat(t,", ")+"sortedDataRowIndices.length=".concat(n.length))}var i=Object(v.b)(e,r,o),c=i.contents,s=i.styles,l=i.type;return{classes:"dataframe ".concat(l),styles:s,contents:Object(y.b)(c)}}}(e,r,0,this.getDataRowIndices()),s=this.getCellRenderer(c),l=this.getDimensions(c),u=l.rowHeight,d=l.headerHeight,f=l.border,b=l.height,p=l.elementWidth,w=l.columnWidth,g=l.headerWidth;return this.recomputeSizeIfNeeded(),h.a.createElement("div",{style:{width:p},className:"dataframe-container stDataFrame"},h.a.createElement(m.MultiGrid,{className:"dataFrame",cellRenderer:s,fixedColumnCount:n,fixedRowCount:r,columnWidth:w,columnCount:a,enableFixedColumnScroll:!0,enableFixedRowScroll:!0,height:b,rowHeight:u,rowCount:i,width:p,classNameBottomLeftGrid:"table-bottom-left",classNameTopRightGrid:"table-top-right",ref:this.multiGridRef}),h.a.createElement("div",{className:"fixup fixup-top-right",style:{width:f,height:d}}),h.a.createElement("div",{className:"fixup fixup-bottom-left",style:{width:g,height:f}}),0===o?h.a.createElement("div",{className:"empty-dataframe"},"empty"):null)}}]),t}(h.a.PureComponent);var j=Object(p.a)(D);r.d(t,"default",function(){return j})}}]);
//# sourceMappingURL=26.8af13474.chunk.js.map