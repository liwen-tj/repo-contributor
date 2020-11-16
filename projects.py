# from urllib import request
import re


def getCNCFProjects():
    # url = 'https://www.cncf.io/projects/'
    # html = request.urlopen(url).read().decode("utf-8")
    html = '''
    <!doctype html>
<html lang="en-US" class="no-focus-outline">

<head>
	<meta charset="UTF-8">
	<meta name=viewport content="width=device-width, initial-scale=1">
	<title>Graduated and incubating projects | Cloud Native Computing Foundation</title>

<!-- The SEO Framework by Sybre Waaijer -->
<meta name="robots" content="max-snippet:-1,max-image-preview:standard,max-video-preview:-1" />
<meta name="description" content="CNCF projects have a maturity level of sandbox, incubating, or graduated, which corresponds to the Innovators, Early Adopters, and Early Majority tiers of the&#8230;" />
<meta property="og:image" content="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-scaled.jpg" />
<meta property="og:image:width" content="2560" />
<meta property="og:image:height" content="615" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="website" />
<meta property="og:title" content="Graduated and incubating projects | Cloud Native Computing Foundation" />
<meta property="og:description" content="CNCF projects have a maturity level of sandbox, incubating, or graduated, which corresponds to the Innovators, Early Adopters, and Early Majority tiers of the Crossing the Chasm diagram." />
<meta property="og:url" content="https://www.cncf.io/projects/" />
<meta property="og:site_name" content="Cloud Native Computing Foundation" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Graduated and incubating projects | Cloud Native Computing Foundation" />
<meta name="twitter:description" content="CNCF projects have a maturity level of sandbox, incubating, or graduated, which corresponds to the Innovators, Early Adopters, and Early Majority tiers of the Crossing the Chasm diagram." />
<meta name="twitter:image" content="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-scaled.jpg" />
<meta name="twitter:image:width" content="2560" />
<meta name="twitter:image:height" content="615" />
<link rel="canonical" href="https://www.cncf.io/projects/" />
<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@id":"https://www.cncf.io/","name":"Cloud Native Computing Foundation"}},{"@type":"ListItem","position":2,"item":{"@id":"https://www.cncf.io/projects/","name":"Graduated and incubating projects"}}]}</script>
<!-- / The SEO Framework by Sybre Waaijer | 6.17ms meta | 0.53ms boot -->

<link rel='dns-prefetch' href='//www.recaptcha.net' />
<link rel='dns-prefetch' href='//www.cncf.io' />
<link crossorigin='' href='//www.googletagmanager.com' rel='preconnect' />
<link crossorigin='' href='//www.gstatic.com' rel='preconnect' />
<link rel='stylesheet' id='wp-block-library-css'  href='https://www.cncf.io/wp/wp-includes/css/dist/block-library/style.min.css?ver=5.5.3' type='text/css' media='all' />
<link rel='stylesheet' id='ctf_styles-css'  href='https://www.cncf.io/wp-content/plugins/custom-twitter-feeds/css/ctf-styles.min.css?ver=1.6.1' type='text/css' media='all' />
<link rel='stylesheet' id='search-filter-plugin-styles-css'  href='https://www.cncf.io/wp-content/plugins/search-filter-pro/public/assets/css/search-filter.min.css?ver=2.5.1' type='text/css' media='all' />
<link rel='stylesheet' id='main-css'  href='https://www.cncf.io/wp-content/themes/lf-theme/build/styles.min.css?ver=1605136055' type='text/css' media='all' />
<link rel="https://api.w.org/" href="https://www.cncf.io/wp-json/" /><link rel="alternate" type="application/json" href="https://www.cncf.io/wp-json/wp/v2/pages/8121" /><!-- Google Tag Manager -->
<script data-type="lazy" data-src="data:text/javascript;base64,KGZ1bmN0aW9uKHcsZCxzLGwsaSl7d1tsXT13W2xdfHxbXTt3W2xdLnB1c2goeydndG0uc3RhcnQnOgpuZXcgRGF0ZSgpLmdldFRpbWUoKSxldmVudDonZ3RtLmpzJ30pO3ZhciBmPWQuZ2V0RWxlbWVudHNCeVRhZ05hbWUocylbMF0sCmo9ZC5jcmVhdGVFbGVtZW50KHMpLGRsPWwhPSdkYXRhTGF5ZXInPycmbD0nK2w6Jyc7ai5hc3luYz10cnVlO2ouc3JjPQonaHR0cHM6Ly93d3cuZ29vZ2xldGFnbWFuYWdlci5jb20vZ3RtLmpzP2lkPScraStkbDtmLnBhcmVudE5vZGUuaW5zZXJ0QmVmb3JlKGosZik7Cn0pKHdpbmRvdyxkb2N1bWVudCwnc2NyaXB0JywnZGF0YUxheWVyJywnR1RNLUtOWEZXVicpOw=="></script>
<!-- End Google Tag Manager -->
		<style type="text/css">
			.um_request_name {
				display: none !important;
			}
		</style>

	<link rel="apple-touch-icon" sizes="180x180"
		href="/wp-content/themes/lf-theme/images/apple-touch-icon.png">
	<link rel="icon" type="image/png" sizes="32x32"
		href="/wp-content/themes/lf-theme/images/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="16x16"
		href="/wp-content/themes/lf-theme/images/favicon-16x16.png">
	<link rel="manifest"
		href="/wp-content/themes/lf-theme/images/site.webmanifest">
	<link rel="mask-icon"
		href="/wp-content/themes/lf-theme/images/safari-pinned-tab.svg">
	<link rel="shortcut icon"
		href="/wp-content/themes/lf-theme/images/favicon.ico">
	<meta name="apple-mobile-web-app-title" content="CNCF">
	<meta name="application-name" content="CNCF">
	<meta name="msapplication-TileColor" content="#de176c">
	<meta name="msapplication-config"
		content="/wp-content/themes/lf-theme/images/browserconfig.xml">
	<meta name="theme-color" content="#ffffff">
	<meta http-equiv="X-UA-Compatible" content="IE=11"><script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={licenseKey:"NRJS-97e2229449e282c1bef",applicationID:"643908501"};window.NREUM||(NREUM={}),__nr_require=function(e,t,n){function r(n){if(!t[n]){var i=t[n]={exports:{}};e[n][0].call(i.exports,function(t){var i=e[n][1][t];return r(i||t)},i,i.exports)}return t[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<n.length;i++)r(n[i]);return r}({1:[function(e,t,n){function r(){}function i(e,t,n){return function(){return o(e,[u.now()].concat(c(arguments)),t?null:this,n),t?void 0:this}}var o=e("handle"),a=e(6),c=e(7),f=e("ee").get("tracer"),u=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",l=p+"ixn-";a(d,function(e,t){s[t]=i(p+t,!0,"api")}),s.addPageAction=i(p+"addPageAction",!0),s.setCurrentRouteName=i(p+"routeName",!0),t.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,t){var n={},r=this,i="function"==typeof t;return o(l+"tracer",[u.now(),e,n],r),function(){if(f.emit((i?"":"no-")+"fn-start",[u.now(),r,i],n),i)try{return t.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],n),e}finally{f.emit("fn-end",[u.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,t){m[t]=i(l+t)}),newrelic.noticeError=function(e,t){"string"==typeof e&&(e=new Error(e)),o("err",[e,u.now(),!1,t])}},{}],2:[function(e,t,n){function r(){return c.exists&&performance.now?Math.round(performance.now()):(o=Math.max((new Date).getTime(),o))-a}function i(){return o}var o=(new Date).getTime(),a=o,c=e(8);t.exports=r,t.exports.offset=a,t.exports.getLastTimestamp=i},{}],3:[function(e,t,n){function r(e,t){var n=e.getEntries();n.forEach(function(e){"first-paint"===e.name?d("timing",["fp",Math.floor(e.startTime)]):"first-contentful-paint"===e.name&&d("timing",["fcp",Math.floor(e.startTime)])})}function i(e,t){var n=e.getEntries();n.length>0&&d("lcp",[n[n.length-1]])}function o(e){e.getEntries().forEach(function(e){e.hadRecentInput||d("cls",[e])})}function a(e){if(e instanceof m&&!g){var t=Math.round(e.timeStamp),n={type:e.type};t<=p.now()?n.fid=p.now()-t:t>p.offset&&t<=Date.now()?(t-=p.offset,n.fid=p.now()-t):t=p.now(),g=!0,d("timing",["fi",t,n])}}function c(e){d("pageHide",[p.now(),e])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var f,u,s,d=e("handle"),p=e("loader"),l=e(5),m=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){f=new PerformanceObserver(r);try{f.observe({entryTypes:["paint"]})}catch(v){}u=new PerformanceObserver(i);try{u.observe({entryTypes:["largest-contentful-paint"]})}catch(v){}s=new PerformanceObserver(o);try{s.observe({type:"layout-shift",buffered:!0})}catch(v){}}if("addEventListener"in document){var g=!1,y=["click","keydown","mousedown","pointerdown","touchstart"];y.forEach(function(e){document.addEventListener(e,a,!1)})}l(c)}},{}],4:[function(e,t,n){function r(e,t){if(!i)return!1;if(e!==i)return!1;if(!t)return!0;if(!o)return!1;for(var n=o.split("."),r=t.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var c=navigator.userAgent,f=c.match(a);f&&c.indexOf("Chrome")===-1&&c.indexOf("Chromium")===-1&&(i="Safari",o=f[1])}t.exports={agent:i,version:o,match:r}},{}],5:[function(e,t,n){function r(e){function t(){e(a&&document[a]?document[a]:document[i]?"hidden":"visible")}"addEventListener"in document&&o&&document.addEventListener(o,t,!1)}t.exports=r;var i,o,a;"undefined"!=typeof document.hidden?(i="hidden",o="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",o="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",o="webkitvisibilitychange",a="webkitVisibilityState")},{}],6:[function(e,t,n){function r(e,t){var n=[],r="",o=0;for(r in e)i.call(e,r)&&(n[o]=t(r,e[r]),o+=1);return n}var i=Object.prototype.hasOwnProperty;t.exports=r},{}],7:[function(e,t,n){function r(e,t,n){t||(t=0),"undefined"==typeof n&&(n=e?e.length:0);for(var r=-1,i=n-t||0,o=Array(i<0?0:i);++r<i;)o[r]=e[t+r];return o}t.exports=r},{}],8:[function(e,t,n){t.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,t,n){function r(){}function i(e){function t(e){return e&&e instanceof r?e:e?f(e,c,o):o()}function n(n,r,i,o){if(!p.aborted||o){e&&e(n,r,i);for(var a=t(i),c=v(n),f=c.length,u=0;u<f;u++)c[u].apply(a,r);var d=s[w[n]];return d&&d.push([b,n,r,a]),a}}function l(e,t){h[e]=v(e).concat(t)}function m(e,t){var n=h[e];if(n)for(var r=0;r<n.length;r++)n[r]===t&&n.splice(r,1)}function v(e){return h[e]||[]}function g(e){return d[e]=d[e]||i(n)}function y(e,t){u(e,function(e,n){t=t||"feature",w[n]=t,t in s||(s[t]=[])})}var h={},w={},b={on:l,addEventListener:l,removeEventListener:m,emit:n,get:g,listeners:v,context:t,buffer:y,abort:a,aborted:!1};return b}function o(){return new r}function a(){(s.api||s.feature)&&(p.aborted=!0,s=p.backlog={})}var c="nr@context",f=e("gos"),u=e(6),s={},d={},p=t.exports=i();p.backlog=s},{}],gos:[function(e,t,n){function r(e,t,n){if(i.call(e,t))return e[t];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return e[t]=r,r}var i=Object.prototype.hasOwnProperty;t.exports=r},{}],handle:[function(e,t,n){function r(e,t,n,r){i.buffer([e],r),i.emit(e,t,n)}var i=e("ee").get("handle");t.exports=r,r.ee=i},{}],id:[function(e,t,n){function r(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===window?0:a(e,o,function(){return i++})}var i=1,o="nr@id",a=e("gos");t.exports=r},{}],loader:[function(e,t,n){function r(){if(!E++){var e=b.info=NREUM.info,t=p.getElementsByTagName("script")[0];if(setTimeout(u.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&t))return u.abort();f(h,function(t,n){e[t]||(e[t]=n)});var n=a();c("mark",["onload",n+b.offset],null,"api"),c("timing",["load",n]);var r=p.createElement("script");r.src="https://"+e.agent,t.parentNode.insertBefore(r,t)}}function i(){"complete"===p.readyState&&o()}function o(){c("mark",["domContent",a()+b.offset],null,"api")}var a=e(2),c=e("handle"),f=e(6),u=e("ee"),s=e(4),d=window,p=d.document,l="addEventListener",m="attachEvent",v=d.XMLHttpRequest,g=v&&v.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:v,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var y=""+location,h={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1184.min.js"},w=v&&g&&g[l]&&!/CriOS/.test(navigator.userAgent),b=t.exports={offset:a.getLastTimestamp(),now:a,origin:y,features:{},xhrWrappable:w,userAgent:s};e(1),e(3),p[l]?(p[l]("DOMContentLoaded",o,!1),d[l]("load",r,!1)):(p[m]("onreadystatechange",i),d[m]("onload",r)),c("mark",["firstbyte",a.getLastTimestamp()],null,"api");var E=0},{}],"wrap-function":[function(e,t,n){function r(e){return!(e&&e instanceof Function&&e.apply&&!e[a])}var i=e("ee"),o=e(7),a="nr@original",c=Object.prototype.hasOwnProperty,f=!1;t.exports=function(e,t){function n(e,t,n,i){function nrWrapper(){var r,a,c,f;try{a=this,r=o(arguments),c="function"==typeof n?n(r,a):n||{}}catch(u){p([u,"",[r,a,i],c])}s(t+"start",[r,a,i],c);try{return f=e.apply(a,r)}catch(d){throw s(t+"err",[r,a,d],c),d}finally{s(t+"end",[r,a,f],c)}}return r(e)?e:(t||(t=""),nrWrapper[a]=e,d(e,nrWrapper),nrWrapper)}function u(e,t,i,o){i||(i="");var a,c,f,u="-"===i.charAt(0);for(f=0;f<t.length;f++)c=t[f],a=e[c],r(a)||(e[c]=n(a,u?c+i:i,o,c))}function s(n,r,i){if(!f||t){var o=f;f=!0;try{e.emit(n,r,i,t)}catch(a){p([a,n,r,i])}f=o}}function d(e,t){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(e);return n.forEach(function(n){Object.defineProperty(t,n,{get:function(){return e[n]},set:function(t){return e[n]=t,t}})}),t}catch(r){p([r])}for(var i in e)c.call(e,i)&&(t[i]=e[i]);return t}function p(t){try{e.emit("internal-error",t)}catch(n){}}return e||(e=i),n.inPlace=u,n.flag=a,n}},{}]},{},["loader"]);</script>
</head>

<body class="page-template-default page page-id-8121 wp-embed-responsive">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KNXFWV"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<div class="hello-bar" role="banner"
	style="background-color: #416fd9; color: #ffffff">
	<div class="container wrap">
		<p>KubeCon + CloudNativeCon North America Virtual | November 17-20, 2020 | Don’t Miss Out | <a href="https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/" target="_blank" rel="noopener">Register Now</a></p>
	</div>
</div>

<header class="site-header">
	<div class="container-full-width wrap">

				<div class="logo">
			<a href="/" title="Cloud Native Computing Foundation">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/cncf-logo.svg"
					height="38" alt="Cloud Native Computing Foundation">
			</a>
		</div>

		<div class="menu-container-with-search" role="navigation">
			<nav class="site-navigation">
				<ul id="menu-main-menu" class="main-navigation"><li id="menu-item-8011" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8011"><a href="#">About</a>
<ul class="sub-menu">
	<li id="menu-item-8083" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8083"><a href="https://www.cncf.io/about/members/">Members</a></li>
	<li id="menu-item-8062" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8062"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/foundation/blob/master/charter.md">Charter</a></li>
	<li id="menu-item-8084" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8084"><a href="https://www.cncf.io/about/join/">Join</a></li>
	<li id="menu-item-8085" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8085"><a href="https://www.cncf.io/about/faq/">FAQ</a></li>
	<li id="menu-item-8087" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8087"><a href="#">Project Journey Reports</a>
	<ul class="sub-menu">
		<li id="menu-item-37988" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-37988"><a href="https://www.cncf.io/cncf-kubernetes-project-journey/">Kubernetes Project Journey</a></li>
		<li id="menu-item-38009" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38009"><a href="https://www.cncf.io/cncf-envoy-project-journey/">Envoy Project Journey</a></li>
		<li id="menu-item-38008" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38008"><a href="https://www.cncf.io/cncf-prometheus-project-journey/">Prometheus Project Journey</a></li>
		<li id="menu-item-38007" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38007"><a href="https://www.cncf.io/cncf-containerd-project-journey/">containerd Project Journey</a></li>
		<li id="menu-item-38006" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38006"><a href="https://www.cncf.io/cncf-fluentd-project-journey/">Fluentd Project Journey</a></li>
		<li id="menu-item-41274" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-41274"><a href="https://www.cncf.io/cncf-jaeger-project-journey-report/">Jaeger Project Journey</a></li>
		<li id="menu-item-41298" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-41298"><a href="https://www.cncf.io/cncf-helm-project-journey-report/">Helm Project Journey</a></li>
	</ul>
</li>
	<li id="menu-item-37989" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-37989"><a target="_blank" rel="noopener noreferrer" href="https://www.cncf.io/wp-content/uploads/2020/08/CNCF_Survey_Report.pdf">Cloud Native Survey 2019</a></li>
	<li id="menu-item-8120" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8120"><a href="#">Annual Reports</a>
	<ul class="sub-menu">
		<li id="menu-item-38012" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38012"><a href="https://www.cncf.io/cncf-annual-report-2019/">CNCF Annual Report 2019</a></li>
		<li id="menu-item-38011" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38011"><a href="https://www.cncf.io/cncf-annual-report-2018/">CNCF Annual Report 2018</a></li>
		<li id="menu-item-38010" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38010"><a href="https://www.cncf.io/cncf-annual-report-2017/">CNCF Annual Report 2017</a></li>
	</ul>
</li>
	<li id="menu-item-8088" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8088"><a href="#">Conference Transparency Reports</a>
	<ul class="sub-menu">
		<li id="menu-item-57994" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-57994"><a href="https://events.linuxfoundation.org/wp-content/uploads/2020/09/KubeCon_EU_20_Report_final.pdf">Europe Virtual August 2020</a></li>
		<li id="menu-item-8089" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8089"><a target="_blank" rel="noopener noreferrer" href="https://events.linuxfoundation.org/wp-content/uploads/2020/02/Kubernetes-Forum-Sydney-Transparency-Report.pdf">Sydney Dec 2019</a></li>
		<li id="menu-item-8090" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8090"><a target="_blank" rel="noopener noreferrer" href="https://events.linuxfoundation.org/wp-content/uploads/2020/02/Kubernetes-Forum-Seoul-Transparency-Report.pdf">Seoul Dec 2019</a></li>
		<li id="menu-item-8091" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8091"><a target="_blank" rel="noopener noreferrer" href="https://www.cncf.io/wp-content/uploads/2020/08/KubeCon_NA_19_Report.pdf">San Diego Nov 2019</a></li>
		<li id="menu-item-38005" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38005"><a target="_blank" rel="noopener noreferrer" href="https://www.cncf.io/wp-content/uploads/2020/08/KubeCon_China_19_Report.pdf">Shanghai June 2019</a></li>
		<li id="menu-item-38031" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38031"><a target="_blank" rel="noopener noreferrer" href="https://www.cncf.io/wp-content/uploads/2020/08/KubeCon_EU_19_Report.pdf">Barcelona May 2019</a></li>
		<li id="menu-item-38032" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38032"><a target="_blank" rel="noopener noreferrer" href="https://www.cncf.io/wp-content/uploads/2020/08/Kubernetes-Day.pdf">Bengaluru March 2019</a></li>
		<li id="menu-item-38033" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38033"><a target="_blank" rel="noopener noreferrer" href="https://www.cncf.io/wp-content/uploads/2020/08/KCCNC-NA-18-Report.pdf">Seattle Dec 2018</a></li>
	</ul>
</li>
	<li id="menu-item-57418" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-57418"><a href="https://www.cncf.io/about/governing-board-meeting-minutes/">Governing Board Meeting Minutes</a></li>
	<li id="menu-item-8092" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8092"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/foundation/blob/master/code-of-conduct.md">Code of conduct</a></li>
	<li id="menu-item-8086" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8086"><a href="https://www.cncf.io/about/contact/">Contact</a></li>
</ul>
</li>
<li id="menu-item-8012" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-ancestor current-menu-parent menu-item-has-children menu-item-8012"><a href="#">Projects</a>
<ul class="sub-menu">
	<li id="menu-item-8081" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8081"><a href="https://www.cncf.io/services-for-projects/">Services for CNCF projects</a></li>
	<li id="menu-item-8129" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-8121 current_page_item menu-item-8129"><a href="https://www.cncf.io/projects/" aria-current="page">Graduated &#038; incubating projects</a></li>
	<li id="menu-item-8020" class="lf-projects-graduated menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8020"><a href="#">Graduated projects</a>
	<ul class="sub-menu">
		<li id="menu-item-35935" class="menu-item menu-item-type-project menu-item-object-link menu-item-35935"><a title="Visit containerd" target="_blank" rel="noopener noreferrer" href="http://containerd.io/">containerd</a></li>
		<li id="menu-item-35934" class="menu-item menu-item-type-project menu-item-object-link menu-item-35934"><a title="Visit CoreDNS" target="_blank" rel="noopener noreferrer" href="https://coredns.io/">CoreDNS</a></li>
		<li id="menu-item-35933" class="menu-item menu-item-type-project menu-item-object-link menu-item-35933"><a title="Visit Envoy" target="_blank" rel="noopener noreferrer" href="https://www.envoyproxy.io/">Envoy</a></li>
		<li id="menu-item-35936" class="menu-item menu-item-type-project menu-item-object-link menu-item-35936"><a title="Visit Fluentd" target="_blank" rel="noopener noreferrer" href="http://fluentd.org/">Fluentd</a></li>
		<li id="menu-item-41123" class="menu-item menu-item-type-project menu-item-object-link menu-item-41123"><a title="Visit Harbor" target="_blank" rel="noopener noreferrer" href="https://goharbor.io/">Harbor</a></li>
		<li id="menu-item-35940" class="menu-item menu-item-type-project menu-item-object-link menu-item-35940"><a title="Visit Helm" target="_blank" rel="noopener noreferrer" href="https://www.helm.sh/">Helm</a></li>
		<li id="menu-item-35937" class="menu-item menu-item-type-project menu-item-object-link menu-item-35937"><a title="Visit Jaeger" target="_blank" rel="noopener noreferrer" href="https://jaegertracing.io/">Jaeger</a></li>
		<li id="menu-item-35931" class="menu-item menu-item-type-project menu-item-object-link menu-item-35931"><a title="Visit Kubernetes" target="_blank" rel="noopener noreferrer" href="http://kubernetes.io/">Kubernetes</a></li>
		<li id="menu-item-35932" class="menu-item menu-item-type-project menu-item-object-link menu-item-35932"><a title="Visit Prometheus" target="_blank" rel="noopener noreferrer" href="https://prometheus.io/">Prometheus</a></li>
		<li id="menu-item-35947" class="menu-item menu-item-type-project menu-item-object-link menu-item-35947"><a title="Visit Rook" target="_blank" rel="noopener noreferrer" href="https://rook.io/">Rook</a></li>
		<li id="menu-item-35952" class="menu-item menu-item-type-project menu-item-object-link menu-item-35952"><a title="Visit TiKV" target="_blank" rel="noopener noreferrer" href="https://tikv.org/">TiKV</a></li>
		<li id="menu-item-35939" class="menu-item menu-item-type-project menu-item-object-link menu-item-35939"><a title="Visit TUF" target="_blank" rel="noopener noreferrer" href="https://theupdateframework.io/">TUF</a></li>
		<li id="menu-item-35938" class="menu-item menu-item-type-project menu-item-object-link menu-item-35938"><a title="Visit Vitess" target="_blank" rel="noopener noreferrer" href="https://vitess.io/">Vitess</a></li>
	</ul>
</li>
	<li id="menu-item-8021" class="lf-projects-incubating menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8021"><a href="#">Incubating projects</a>
	<ul class="sub-menu">
		<li id="menu-item-35955" class="menu-item menu-item-type-project menu-item-object-link menu-item-35955"><a title="Visit Argo" target="_blank" rel="noopener noreferrer" href="https://argoproj.github.io/">Argo</a></li>
		<li id="menu-item-35953" class="menu-item menu-item-type-project menu-item-object-link menu-item-35953"><a title="Visit CloudEvents" target="_blank" rel="noopener noreferrer" href="https://cloudevents.io/">CloudEvents</a></li>
		<li id="menu-item-35943" class="menu-item menu-item-type-project menu-item-object-link menu-item-35943"><a title="Visit CNI" target="_blank" rel="noopener noreferrer" href="https://github.com/containernetworking">CNI</a></li>
		<li id="menu-item-41132" class="menu-item menu-item-type-project menu-item-object-link menu-item-41132"><a title="Visit Contour" target="_blank" rel="noopener noreferrer" href="https://projectcontour.io/">Contour</a></li>
		<li id="menu-item-41141" class="menu-item menu-item-type-project menu-item-object-link menu-item-41141"><a title="Visit Cortex" target="_blank" rel="noopener noreferrer" href="https://github.com/cortexproject">Cortex</a></li>
		<li id="menu-item-35951" class="menu-item menu-item-type-project menu-item-object-link menu-item-35951"><a title="Visit CRI-O" target="_blank" rel="noopener noreferrer" href="https://cri-o.io/">CRI-O</a></li>
		<li id="menu-item-35956" class="menu-item menu-item-type-project menu-item-object-link menu-item-35956"><a title="Visit Dragonfly" target="_blank" rel="noopener noreferrer" href="https://d7y.io/">Dragonfly</a></li>
		<li id="menu-item-35949" class="menu-item menu-item-type-project menu-item-object-link menu-item-35949"><a title="Visit etcd" target="_blank" rel="noopener noreferrer" href="https://etcd.io/">etcd</a></li>
		<li id="menu-item-35954" class="menu-item menu-item-type-project menu-item-object-link menu-item-35954"><a title="Visit Falco" target="_blank" rel="noopener noreferrer" href="https://falco.org/">Falco</a></li>
		<li id="menu-item-35942" class="menu-item menu-item-type-project menu-item-object-link menu-item-35942"><a title="Visit gRPC" target="_blank" rel="noopener noreferrer" href="https://grpc.io/">gRPC</a></li>
		<li id="menu-item-35964" class="menu-item menu-item-type-project menu-item-object-link menu-item-35964"><a title="Visit KubeEdge" target="_blank" rel="noopener noreferrer" href="https://kubeedge.io/en/">KubeEdge</a></li>
		<li id="menu-item-35946" class="menu-item menu-item-type-project menu-item-object-link menu-item-35946"><a title="Visit Linkerd" target="_blank" rel="noopener noreferrer" href="https://linkerd.io/">Linkerd</a></li>
		<li id="menu-item-35945" class="menu-item menu-item-type-project menu-item-object-link menu-item-35945"><a title="Visit NATS" target="_blank" rel="noopener noreferrer" href="https://nats.io/">NATS</a></li>
		<li id="menu-item-35944" class="menu-item menu-item-type-project menu-item-object-link menu-item-35944"><a title="Visit Notary" target="_blank" rel="noopener noreferrer" href="https://github.com/theupdateframework/notary">Notary</a></li>
		<li id="menu-item-35950" class="menu-item menu-item-type-project menu-item-object-link menu-item-35950"><a title="Visit Open Policy Agent" target="_blank" rel="noopener noreferrer" href="http://www.openpolicyagent.org/">Open Policy Agent</a></li>
		<li id="menu-item-35941" class="menu-item menu-item-type-project menu-item-object-link menu-item-35941"><a title="Visit OpenTracing" target="_blank" rel="noopener noreferrer" href="http://opentracing.io/">OpenTracing</a></li>
		<li id="menu-item-41135" class="menu-item menu-item-type-project menu-item-object-link menu-item-41135"><a title="Visit Operator Framework" target="_blank" rel="noopener noreferrer" href="https://operatorframework.io/">Operator Framework</a></li>
		<li id="menu-item-41126" class="menu-item menu-item-type-project menu-item-object-link menu-item-41126"><a title="Visit SPIFFE" target="_blank" rel="noopener noreferrer" href="https://spiffe.io/">SPIFFE</a></li>
		<li id="menu-item-41129" class="menu-item menu-item-type-project menu-item-object-link menu-item-41129"><a title="Visit SPIRE" target="_blank" rel="noopener noreferrer" href="https://github.com/spiffe/spire">SPIRE</a></li>
		<li id="menu-item-41138" class="menu-item menu-item-type-project menu-item-object-link menu-item-41138"><a title="Visit Thanos" target="_blank" rel="noopener noreferrer" href="https://thanos.io/">Thanos</a></li>
	</ul>
</li>
	<li id="menu-item-8128" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8128"><a href="https://www.cncf.io/sandbox-projects/">All Sandbox projects</a></li>
	<li id="menu-item-8127" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8127"><a href="https://www.cncf.io/archived-projects/">Archived projects</a></li>
	<li id="menu-item-8069" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8069"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/toc/blob/master/DEFINITION.md">Cloud native definition</a></li>
	<li id="menu-item-8070" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8070"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/landscape/blob/master/README.md#trail-map">Cloud Native Trail Map</a></li>
	<li id="menu-item-8071" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8071"><a target="_blank" rel="noopener noreferrer" href="https://landscape.cncf.io/">Interactive Landscape</a></li>
	<li id="menu-item-57490" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-57490"><a target="_blank" rel="noopener noreferrer" href="https://radar.cncf.io/">End User Tech Radar</a></li>
	<li id="menu-item-8072" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8072"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/toc/blob/master/PRINCIPLES.md">TOC principles</a></li>
	<li id="menu-item-8073" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8073"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/contribute/blob/master/README.md">Contribution guides</a></li>
	<li id="menu-item-8074" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8074"><a href="#">Project tools</a>
	<ul class="sub-menu">
		<li id="menu-item-8075" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8075"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/foundation/blob/master/code-of-conduct.md">Code of conduct</a></li>
		<li id="menu-item-8076" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8076"><a target="_blank" rel="noopener noreferrer" href="https://cncf.ci/">Continuous integration</a></li>
		<li id="menu-item-8077" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8077"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/toc/blob/master/process/graduation_criteria.adoc">Graduation criteria</a></li>
		<li id="menu-item-8078" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8078"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/foundation/blob/master/website-guidelines.md">Website guidelines</a></li>
		<li id="menu-item-8079" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8079"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/foundation/blob/master/copyright-notices.md">Copyright notices</a></li>
		<li id="menu-item-8080" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8080"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/toc/blob/master/process/project_proposals.adoc">Propose project</a></li>
	</ul>
</li>
</ul>
</li>
<li id="menu-item-8013" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8013"><a href="#">Certification</a>
<ul class="sub-menu">
	<li id="menu-item-8145" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8145"><a href="https://www.cncf.io/certification/software-conformance/">Software conformance<br>(Certified Kubernetes)</a></li>
	<li id="menu-item-8144" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8144"><a href="https://www.cncf.io/certification/training/">Training</a></li>
	<li id="menu-item-8143" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8143"><a href="https://www.cncf.io/certification/cka/">Certified Kubernetes Administrator (CKA)</a></li>
	<li id="menu-item-39216" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-39216"><a href="https://www.cncf.io/certification/ckad/">Certified Kubernetes Application Developer (CKAD)</a></li>
	<li id="menu-item-8141" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8141"><a href="https://www.cncf.io/certification/kcsp/">Kubernetes Certified Service Provider (KCSP)</a></li>
</ul>
</li>
<li id="menu-item-8014" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8014"><a href="#">People</a>
<ul class="sub-menu">
	<li id="menu-item-24495" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24495"><a href="https://www.cncf.io/people/end-user-community/">End User Community</a></li>
	<li id="menu-item-8100" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8100"><a href="https://www.cncf.io/people/technical-oversight-committee/">Technical Oversight Committee</a></li>
	<li id="menu-item-24496" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24496"><a href="https://www.cncf.io/people/governing-board/">Governing Board</a></li>
	<li id="menu-item-24494" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24494"><a href="https://www.cncf.io/people/ambassadors/">Ambassadors</a></li>
	<li id="menu-item-24497" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-24497"><a href="https://www.cncf.io/people/staff/">Staff</a></li>
</ul>
</li>
<li id="menu-item-8015" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8015"><a href="#">Community</a>
<ul class="sub-menu">
	<li id="menu-item-8146" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8146"><a href="https://www.cncf.io/kubecon-cloudnativecon-events/">KubeCon + CloudNativeCon and other CNCF events</a></li>
	<li id="menu-item-8165" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8165"><a href="https://www.cncf.io/events/">Events we’ll be at</a></li>
	<li id="menu-item-38028" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38028"><a href="https://www.cncf.io/phippy/">Phippy and friends</a></li>
	<li id="menu-item-31860" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31860"><a href="https://www.cncf.io/spotlights/">Community spotlight</a></li>
	<li id="menu-item-8114" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8114"><a target="_blank" rel="noopener noreferrer" href="https://jobs.cncf.io/">Job board</a></li>
	<li id="menu-item-10826" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10826"><a href="https://www.cncf.io/webinars/">Webinars</a></li>
	<li id="menu-item-10825" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-10825"><a href="https://www.cncf.io/speakers/">Speakers Bureau</a></li>
	<li id="menu-item-38027" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38027"><a href="https://www.cncf.io/community-infrastructure-lab/">Community Infrastructure Lab</a></li>
	<li id="menu-item-40717" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-40717"><a href="#">Meet</a>
	<ul class="sub-menu">
		<li id="menu-item-38029" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38029"><a href="https://www.cncf.io/telecom-user-group/">Telecom User Group</a></li>
		<li id="menu-item-8115" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8115"><a target="_blank" rel="noopener noreferrer" href="https://kubernetescommunitydays.org/">Kubernetes Community Days</a></li>
		<li id="menu-item-8116" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8116"><a target="_blank" rel="noopener noreferrer" href="https://community.cncf.io/">Meetups</a></li>
		<li id="menu-item-38026" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-38026"><a href="https://www.cncf.io/calendar/">Calendar</a></li>
	</ul>
</li>
	<li id="menu-item-8117" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8117"><a target="_blank" rel="noopener noreferrer" href="https://slack.cncf.io">Slack</a></li>
	<li id="menu-item-8118" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8118"><a target="_blank" rel="noopener noreferrer" href="https://lists.cncf.io/g/main/subgroups">Mailing lists</a></li>
	<li id="menu-item-8119" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8119"><a target="_blank" rel="noopener noreferrer" href="https://store.cncf.io/">Store</a></li>
</ul>
</li>
<li id="menu-item-8016" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-8016"><a href="#">Newsroom</a>
<ul class="sub-menu">
	<li id="menu-item-12260" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-12260"><a href="/announcements">Announcements</a></li>
	<li id="menu-item-12258" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-12258"><a href="/blog">Blog</a></li>
	<li id="menu-item-12259" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-12259"><a href="/news">In the news</a></li>
	<li id="menu-item-8161" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8161"><a href="https://www.cncf.io/case-studies/">End user case studies</a></li>
	<li id="menu-item-8160" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-8160"><a href="https://www.cncf.io/case-studies-cn/">最终用户案例研究</a></li>
	<li id="menu-item-8108" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8108"><a target="_blank" rel="noopener noreferrer" href="https://docs.google.com/presentation/d/1UGewu4MMYZobunfKr5sOGXsspcLOH_5XeCLyOHKh9LU/edit?usp=sharing">Overview slides</a></li>
	<li id="menu-item-8109" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8109"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/artwork">Project logos</a></li>
	<li id="menu-item-8110" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8110"><a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/c/cloudnativefdn">Videos</a></li>
	<li id="menu-item-8111" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8111"><a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/143247548@N03/albums/with/72157676361993185">Pictures</a></li>
	<li id="menu-item-8112" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8112"><a target="_blank" rel="noopener noreferrer" href="https://github.com/cncf/foundation/blob/master/style-guide.md">Style guide</a></li>
	<li id="menu-item-8113" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-8113"><a target="_blank" rel="noopener noreferrer" href="https://www.linuxfoundation.org/trademark-usage">Trademark</a></li>
</ul>
</li>
</ul>
								<div class="header-cta">
					<a href="https://www.cncf.io/about/join/"
						class="button header-align">Join Now</a>
				</div>

				<div class="header-search">
					<button
						class="button						search-toggle						search-button						header-align"
						type="button" aria-label="Search">
						<svg height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg" aria-labelledby="search-title"><title id="search-title">Search</title><path fill="currentColor" d="m21.172 24-7.387-7.387c-1.388.874-3.024 1.387-4.785 1.387-4.971 0-9-4.029-9-9s4.029-9 9-9 9 4.029 9 9c0 1.761-.514 3.398-1.387 4.785l7.387 7.387zm-12.172-8c3.859 0 7-3.14 7-7s-3.141-7-7-7-7 3.14-7 7 3.141 7 7 7z"/></svg>					</button>

					<div class="search-bar">
						<div class="container-full-width wrap search-wrapper">
							<form class="search-form" method="get"
								action="https://www.cncf.io"
								role="search">
								<label for="search-bar"
									class="screen-reader-text">Search
									CNCF</label>
								<input class="search-input" type="search"
									id="search-bar"
									value=""
									name="s" placeholder="Search for..."
									title="Search for" autocomplete="off"
									autocorrect="off" autocapitalize="off"
									spellcheck="false"
									maxlength="98"
									required>
								<label>
									<input class="button transparent									header-align									search-submit"
										type="submit" value="Search" />
								</label>
							</form>
							<button
							class="button							search-toggle							search-button							header-align"
							type="button" aria-label="Close">
								<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewbox="0 0 24 24" aria-labelledby="close-title"><title id="close-title">Close</title><path d="M24 20.188l-8.315-8.209 8.2-8.282-3.697-3.697-8.212 8.318-8.31-8.203-3.666 3.666 8.321 8.24-8.206 8.313 3.666 3.666 8.237-8.318 8.285 8.203z"/></svg>							</button>
						</div>

					</div>
				</div>
			</nav>
		</div>

		<button class="hamburger hamburger--spin" type="button"
			aria-label="Toggle Menu">
			<span class="hamburger-box">
				<span class="hamburger-inner"></span>
			</span>
		</button>

	</div>
</header>

<section class="hero background-image-wrapper">

	<figure class="background-image-figure">
	<picture><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-2880x520.jpg" media="(min-width: 2880px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-1920x260.jpg" media="(min-width: 1920px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-1440x260.jpg" media="(min-width: 1440px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-1200x220.jpg" media="(min-width: 1200px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-1024x220.jpg" media="(min-width: 1024px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-768x220.jpg" media="(min-width: 768px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-600x220.jpg" media="(min-width: 600px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-414x220.jpg" media="(min-width: 414px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-375x220.jpg" media="(min-width: 375px)"><source srcset="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-320x220.jpg" media="(min-width: 0px)">
		<img src="https://www.cncf.io/wp-content/uploads/2020/08/fotis-fotopoulos-DuHKoV44prg-unsplash-320x220.jpg" class="" alt="">
		</picture>	</figure>

	<div class="container wrap background-image-text-overlay">
		<div>
						<h1 class="page-title" itemprop="headline">Graduated and incubating projects			</h1>
					</div>
	</div>
</section>

<main class="page-content">
	<article class="container wrap entry-content">

<h3>Graduated</h3>



<div class="projects-wrapper">
			<div class="project-box">
		<!-- thumbnail  -->
							<a href="http://containerd.io/"  rel="noopener" target="_blank" title="containerd (accepted to CNCF on 3/29/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/containerd.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="http://containerd.io/"  rel="noopener" target="_blank" title="Visit containerd">
				containerd			</a>

		</h3>

					<span class="project-category">
				Container Runtime</span>

		<div class="project-icons">

						<a title="containerd on Github"
				href="https://github.com/containerd/containerd"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="containerd on DevStats"
				href="https://containerd.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="containerd Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/graduated.md#containerd-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="containerd on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/containerd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="containerd on Twitter"
				href="https://twitter.com/containerd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>



						<a title="containerd Slack"
				href="https://slack.containerd.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://coredns.io/"  rel="noopener" target="_blank" title="CoreDNS (accepted to CNCF on 2/27/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/coredns.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://coredns.io/"  rel="noopener" target="_blank" title="Visit CoreDNS">
				CoreDNS			</a>

		</h3>

					<span class="project-category">
				Service Discovery</span>

		<div class="project-icons">

						<a title="CoreDNS on Github"
				href="https://github.com/coredns/coredns"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="CoreDNS on DevStats"
				href="https://coredns.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="CoreDNS Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/graduated.md#coredns-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="CoreDNS on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/coredns"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="CoreDNS on Twitter"
				href="https://twitter.com/corednsio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="CoreDNS Blog"
				href="https://blog.coredns.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="CoreDNS Contact"
				href="https://groups.google.com/forum/#!forum/coredns-discuss"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>

						<a title="CoreDNS Slack"
				href="https://cloud-native.slack.com/messages/coredns/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>

						<a title="CoreDNS on YouTube"
				href="https://www.youtube.com/channel/UCbWRJZxiaQ8twm6sh7UymoQ"
				 rel="noopener" target="_blank"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a>


		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://www.envoyproxy.io/"  rel="noopener" target="_blank" title="Envoy (accepted to CNCF on 9/13/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/envoy.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://www.envoyproxy.io/"  rel="noopener" target="_blank" title="Visit Envoy">
				Envoy			</a>

		</h3>

					<span class="project-category">
				Network Proxy</span>

		<div class="project-icons">

						<a title="Envoy on Github"
				href="https://github.com/envoyproxy/envoy"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Envoy on DevStats"
				href="https://envoy.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Envoy Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/graduated.md#envoy-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Envoy on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/envoyproxy"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Envoy on Twitter"
				href="https://twitter.com/EnvoyProxy/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>



						<a title="Envoy Slack"
				href="http://envoyslack.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="http://fluentd.org/"  rel="noopener" target="_blank" title="Fluentd (accepted to CNCF on 11/8/2016)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/fluentd.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="http://fluentd.org/"  rel="noopener" target="_blank" title="Visit Fluentd">
				Fluentd			</a>

		</h3>

					<span class="project-category">
				Logging</span>

		<div class="project-icons">

						<a title="Fluentd on Github"
				href="https://github.com/fluent/fluentd/"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Fluentd on DevStats"
				href="https://fluentd.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Fluentd Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/graduated.md#fluentd-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Fluentd on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/fluentd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Fluentd on Twitter"
				href="https://twitter.com/fluentd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Fluentd Blog"
				href="http://www.fluentd.org/blog/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>


						<a title="Fluentd Slack"
				href="http://slack.fluentd.org/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://goharbor.io/"  rel="noopener" target="_blank" title="Harbor (accepted to CNCF on 7/31/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/harbor-icon.svg" class="project-thumbnail" alt="" loading="lazy" height="100.36" width="99.73" />				</a>

		<h3 class="project-title">

					<a href="https://goharbor.io/"  rel="noopener" target="_blank" title="Visit Harbor">
				Harbor			</a>

		</h3>

					<span class="project-category">
				Registry</span>

		<div class="project-icons">

						<a title="Harbor on Github"
				href="https://github.com/goharbor"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Harbor on DevStats"
				href="https://harbor.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Harbor Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#harbor-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Harbor on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/harbor"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Harbor on Twitter"
				href="https://twitter.com/project_harbor"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>


						<a title="Harbor Contact"
				href="https://lists.cncf.io/g/harbor-users/topics"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>

						<a title="Harbor Slack"
				href="https://cloud-native.slack.com/messages/harbor/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://www.helm.sh/"  rel="noopener" target="_blank" title="Helm (accepted to CNCF on 6/1/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/helm.svg" class="project-thumbnail" alt="" loading="lazy" height="129.1199951" width="124" />				</a>

		<h3 class="project-title">

					<a href="https://www.helm.sh/"  rel="noopener" target="_blank" title="Visit Helm">
				Helm			</a>

		</h3>

					<span class="project-category">
				Package Management</span>

		<div class="project-icons">

						<a title="Helm on Github"
				href="https://github.com/kubernetes/helm"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Helm on DevStats"
				href="https://helm.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Helm Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#helm-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Helm on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/helm"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Helm on Twitter"
				href="https://twitter.com/helmpack"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>






		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://jaegertracing.io/"  rel="noopener" target="_blank" title="Jaeger (accepted to CNCF on 9/13/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/jaeger.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://jaegertracing.io/"  rel="noopener" target="_blank" title="Visit Jaeger">
				Jaeger			</a>

		</h3>

					<span class="project-category">
				Distributed Tracing</span>

		<div class="project-icons">

						<a title="Jaeger on Github"
				href="https://github.com/uber/jaeger"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Jaeger on DevStats"
				href="https://jaeger.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Jaeger Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#jaeger-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Jaeger on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/jaeger"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Jaeger on Twitter"
				href="https://twitter.com/JaegerTracing"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Jaeger Blog"
				href="https://medium.com/jaegertracing/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="Jaeger Contact"
				href="https://groups.google.com/forum/#!forum/jaeger-tracing"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>



						<a title="Jaeger on Gitter"
				href="https://gitter.im/jaegertracing/Lobby"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>Gitter</title>
 <g>
  <rect id="svg_1" fill="currentColor" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2" fill="#FFF">
   <path class="inner-color" stroke="null" id="svg_3" d="m189.043259,281.800446c0,-57.955597 0.307602,-115.911194 -0.242386,-173.857445c-0.121185,-12.687393 4.055099,-16.89167 16.621368,-16.602669c35.657059,0.820328 29.933289,-2.61953 30.007828,30.436691q0.354263,166.61409 0.0746,333.218887c0,17.339142 -0.083923,17.525604 -17.497665,17.404419c-32.646027,-0.233063 -28.814606,3.859314 -28.926483,-28.600311c-0.16777,-54.002991 -0.046585,-107.996582 -0.037262,-161.999573zm89.445694,-0.037354c0,-57.955551 0.326202,-115.911118 -0.242401,-173.857361c-0.130524,-12.706062 3.989868,-16.854401 16.556061,-16.565399c35.218964,0.811043 30.035858,-2.638161 30.091766,30.473999q0.298279,165.95224 0.065277,331.90451c0,18.662781 -0.065277,18.830627 -19.119659,18.690735c-31.378204,-0.24231 -27.164642,3.477173 -27.285828,-27.332336c-0.223785,-54.441193 -0.065216,-108.882294 -0.065216,-163.323456l0,0.009308zm-174.155746,-116.032303c0.009354,-41.716446 0.410202,-83.432915 -0.233025,-125.140034c-0.186455,-12.305187 4.092392,-15.912853 15.922165,-15.567947c35.228264,0.988171 30.641777,-4.204273 30.734978,31.024014c0.214432,78.156578 0.083923,156.313194 0.046616,234.479088c0,17.180664 -0.428802,17.609467 -17.805222,17.646729c-33.895218,0.065308 -28.376511,1.258514 -28.590942,-27.835815c-0.279648,-38.202026 -0.065216,-76.404022 -0.065216,-114.606033l-0.009354,0zm258.85643,33.485016c0.009308,-31.163803 0.251709,-62.336975 -0.130524,-93.500778c-0.121185,-9.900085 3.020355,-14.402679 13.51712,-14.272171c39.712128,0.475449 32.757904,-3.141533 32.990906,31.340942c0.382202,55.746262 0.121185,111.492477 0.093231,167.238693c-0.009308,17.767944 -0.251709,18.103577 -17.245972,18.131531c-33.997711,0.065277 -28.917084,1.883026 -29.178101,-28.618896c-0.233093,-26.763794 -0.046661,-53.546204 -0.046661,-80.319321z"/>
  </g>
 </g>
</svg></a>

		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="http://kubernetes.io/"  rel="noopener" target="_blank" title="Kubernetes (accepted to CNCF on 3/16/2016)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/kubernetes.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="http://kubernetes.io/"  rel="noopener" target="_blank" title="Visit Kubernetes">
				Kubernetes			</a>

		</h3>

					<span class="project-category">
				Orchestration</span>

		<div class="project-icons">

						<a title="Kubernetes on Github"
				href="https://github.com/kubernetes"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Kubernetes on DevStats"
				href="https://k8s.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Kubernetes Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/graduated.md#kubernetes-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Kubernetes on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/kubernetes"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Kubernetes on Twitter"
				href="https://twitter.com/kubernetesio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Kubernetes Blog"
				href="http://blog.kubernetes.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="Kubernetes Contact"
				href="https://groups.google.com/forum/#!forum/kubernetes-dev"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>

						<a title="Kubernetes Slack"
				href="http://slack.k8s.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>

						<a title="Kubernetes on YouTube"
				href="https://www.youtube.com/channel/UCZ2bu0qutTOM0tHYa_jkIwg"
				 rel="noopener" target="_blank"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a>


		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://prometheus.io/"  rel="noopener" target="_blank" title="Prometheus (accepted to CNCF on 5/9/2016)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/prometheus.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://prometheus.io/"  rel="noopener" target="_blank" title="Visit Prometheus">
				Prometheus			</a>

		</h3>

					<span class="project-category">
				Monitoring</span>

		<div class="project-icons">

						<a title="Prometheus on Github"
				href="https://github.com/prometheus"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Prometheus on DevStats"
				href="https://prometheus.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Prometheus Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/graduated.md#prometheus-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Prometheus on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/prometheus"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Prometheus on Twitter"
				href="https://twitter.com/prometheusio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Prometheus Blog"
				href="https://prometheus.io/blog/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="Prometheus Contact"
				href="https://prometheus.io/community/"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>


						<a title="Prometheus on YouTube"
				href="https://www.youtube.com/channel/UC4pLFely0-Odea4B2NL1nWA"
				 rel="noopener" target="_blank"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a>


		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://rook.io/"  rel="noopener" target="_blank" title="Rook (accepted to CNCF on 1/29/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/rook.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://rook.io/"  rel="noopener" target="_blank" title="Visit Rook">
				Rook			</a>

		</h3>

					<span class="project-category">
				Storage</span>

		<div class="project-icons">

						<a title="Rook on Github"
				href="https://github.com/rook/rook"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Rook on DevStats"
				href="https://rook.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Rook Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#rook-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Rook on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/rook"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Rook on Twitter"
				href="https://twitter.com/rook_io"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Rook Blog"
				href="https://blog.rook.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>


						<a title="Rook Slack"
				href="https://rook-io.slack.com/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://tikv.org/"  rel="noopener" target="_blank" title="TiKV (accepted to CNCF on 8/28/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/tikv.svg" class="project-thumbnail" alt="" loading="lazy" height="360" width="360" />				</a>

		<h3 class="project-title">

					<a href="https://tikv.org/"  rel="noopener" target="_blank" title="Visit TiKV">
				TiKV			</a>

		</h3>

					<span class="project-category">
				Key/Value Store</span>

		<div class="project-icons">

						<a title="TiKV on Github"
				href="https://github.com/tikv/tikv"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="TiKV on DevStats"
				href="https://tikv.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="TiKV Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#tikv-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="TiKV on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/tikv"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="TiKV on Twitter"
				href="https://twitter.com/tikvproject"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="TiKV Blog"
				href="https://tikv.org/blog/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="TiKV Contact"
				href="https://tikv.org/community/community/"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>


						<a title="TiKV on YouTube"
				href="https://www.youtube.com/channel/UCXyuUR4qEm0HLDniz46k6sg"
				 rel="noopener" target="_blank"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a>


		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://theupdateframework.io/"  rel="noopener" target="_blank" title="TUF (accepted to CNCF on 10/24/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/tuf.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://theupdateframework.io/"  rel="noopener" target="_blank" title="Visit TUF">
				TUF			</a>

		</h3>

					<span class="project-category">
				Software Update Spec</span>

		<div class="project-icons">

						<a title="TUF on Github"
				href="https://github.com/theupdateframework/specification"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="TUF on DevStats"
				href="https://tuf.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="TUF Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#tuf-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="TUF on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/the-update-framework"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>



						<a title="TUF Contact"
				href="https://groups.google.com/forum/?fromgroups#!forum/theupdateframework"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>




		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://vitess.io/"  rel="noopener" target="_blank" title="Vitess (accepted to CNCF on 2/5/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/vitess.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://vitess.io/"  rel="noopener" target="_blank" title="Visit Vitess">
				Vitess			</a>

		</h3>

					<span class="project-category">
				Storage</span>

		<div class="project-icons">

						<a title="Vitess on Github"
				href="https://github.com/vitessio/vitess"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Vitess on DevStats"
				href="https://vitess.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Vitess Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#vitess-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Vitess on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/vitess"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Vitess on Twitter"
				href="https://twitter.com/vitessio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Vitess Blog"
				href="http://blog.vitess.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="Vitess Contact"
				href="https://groups.google.com/forum/#!forum/vitess"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>




		</div>

	</div>
			</div>




<div style="height:100px" aria-hidden="true" class="wp-block-spacer is-style-40-responsive"></div>



<h3>Incubating</h3>



<div class="projects-wrapper">
			<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://argoproj.github.io/"  rel="noopener" target="_blank" title="Argo (accepted to CNCF on 4/7/2020)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/argo.svg" class="project-thumbnail" alt="" loading="lazy" height="360" width="360" />				</a>

		<h3 class="project-title">

					<a href="https://argoproj.github.io/"  rel="noopener" target="_blank" title="Visit Argo">
				Argo			</a>

		</h3>

					<span class="project-category">
				Continuous Integration &amp; Deployment</span>

		<div class="project-icons">

						<a title="Argo on Github"
				href="https://github.com/argoproj"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Argo on DevStats"
				href="https://argo.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Argo Logos"
				href="https://github.com/cncf/artwork/tree/master/projects/argo"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>








		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://cloudevents.io/"  rel="noopener" target="_blank" title="CloudEvents (accepted to CNCF on 5/22/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/cloudevents.svg" class="project-thumbnail" alt="" loading="lazy" height="360" width="360" />				</a>

		<h3 class="project-title">

					<a href="https://cloudevents.io/"  rel="noopener" target="_blank" title="Visit CloudEvents">
				CloudEvents			</a>

		</h3>

					<span class="project-category">
				Serverless</span>

		<div class="project-icons">

						<a title="CloudEvents on Github"
				href="https://github.com/cloudevents/spec"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="CloudEvents on DevStats"
				href="https://cloudevents.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="CloudEvents Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#cloudevents-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="CloudEvents on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/cloudevents"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="CloudEvents on Twitter"
				href="https://twitter.com/cloudeventsio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>



						<a title="CloudEvents Slack"
				href="https://cloud-native.slack.com/messages/cloudevents"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://github.com/containernetworking"  rel="noopener" target="_blank" title="CNI (accepted to CNCF on 5/23/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/CNI.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://github.com/containernetworking"  rel="noopener" target="_blank" title="Visit CNI">
				CNI			</a>

		</h3>

					<span class="project-category">
				Networking API</span>

		<div class="project-icons">

						<a title="CNI on Github"
				href="https://github.com/containernetworking"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="CNI on DevStats"
				href="https://cni.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="CNI Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#cni-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="CNI on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/cni"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>



						<a title="CNI Contact"
				href="https://groups.google.com/forum/#!forum/cni-dev"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>

						<a title="CNI Slack"
				href="https://containernetworking.slack.com/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://projectcontour.io/"  rel="noopener" target="_blank" title="Contour (accepted to CNCF on 7/7/2020)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/contour-icon-color.svg" class="project-thumbnail" alt="" loading="lazy" height="361.14" width="361.14" />				</a>

		<h3 class="project-title">

					<a href="https://projectcontour.io/"  rel="noopener" target="_blank" title="Visit Contour">
				Contour			</a>

		</h3>

					<span class="project-category">
				High performance ingress controller</span>

		<div class="project-icons">

						<a title="Contour on Github"
				href="https://github.com/projectcontour/contour"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Contour on DevStats"
				href="https://contour.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>









		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://github.com/cortexproject"  rel="noopener" target="_blank" title="Cortex (accepted to CNCF on 9/20/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/cortex.svg" class="project-thumbnail" alt="" loading="lazy" height="243.11" width="243.36" />				</a>

		<h3 class="project-title">

					<a href="https://github.com/cortexproject"  rel="noopener" target="_blank" title="Visit Cortex">
				Cortex			</a>

		</h3>

					<span class="project-category">
				Monitoring</span>

		<div class="project-icons">

						<a title="Cortex on Github"
				href="https://github.com/cortexproject/cortex"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Cortex on DevStats"
				href="https://cortex.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Cortex Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#cortex-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>





						<a title="Cortex Slack"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#cortex-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://cri-o.io/"  rel="noopener" target="_blank" title="CRI-O (accepted to CNCF on 4/8/2019)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/cri-o.svg" class="project-thumbnail" alt="" loading="lazy" height="360" width="360" />				</a>

		<h3 class="project-title">

					<a href="https://cri-o.io/"  rel="noopener" target="_blank" title="Visit CRI-O">
				CRI-O			</a>

		</h3>

					<span class="project-category">
				Container Runtime</span>

		<div class="project-icons">

						<a title="CRI-O on Github"
				href="https://github.com/cri-o/cri-o"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="CRI-O on DevStats"
				href="https://crio.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="CRI-O Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#cri-o-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="CRI-O on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/cri-o"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>


						<a title="CRI-O Blog"
				href="https://medium.com/cri-o"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>


						<a title="CRI-O Slack"
				href="https://kubernetes.slack.com/messages/CAZH62UR1"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://d7y.io/"  rel="noopener" target="_blank" title="Dragonfly (accepted to CNCF on 11/15/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/dragonfly.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://d7y.io/"  rel="noopener" target="_blank" title="Visit Dragonfly">
				Dragonfly			</a>

		</h3>

					<span class="project-category">
				Image Distribution</span>

		<div class="project-icons">

						<a title="Dragonfly on Github"
				href="https://github.com/dragonflyoss/dragonfly"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Dragonfly on DevStats"
				href="https://dragonfly.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Dragonfly Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#dragonfly-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>


						<a title="Dragonfly on Twitter"
				href="https://twitter.com/dragonfly_oss"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>






		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://etcd.io/"  rel="noopener" target="_blank" title="etcd (accepted to CNCF on 12/11/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/etcd.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://etcd.io/"  rel="noopener" target="_blank" title="Visit etcd">
				etcd			</a>

		</h3>

					<span class="project-category">
				Key/Value Store</span>

		<div class="project-icons">

						<a title="etcd on Github"
				href="https://github.com/etcd-io/etcd"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="etcd on DevStats"
				href="https://etcd.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="etcd Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#etcd-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="etcd on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/etcd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>



						<a title="etcd Contact"
				href="https://groups.google.com/forum/?hl=en#!forum/etcd-dev"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>




		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://falco.org/"  rel="noopener" target="_blank" title="Falco (accepted to CNCF on 10/10/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/falco.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://falco.org/"  rel="noopener" target="_blank" title="Visit Falco">
				Falco			</a>

		</h3>

					<span class="project-category">
				Container Security</span>

		<div class="project-icons">

						<a title="Falco on Github"
				href="https://github.com/falcosecurity/falco"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Falco on DevStats"
				href="https://falco.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Falco Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#falco-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>








		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://grpc.io/"  rel="noopener" target="_blank" title="gRPC (accepted to CNCF on 2/16/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/grpc.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://grpc.io/"  rel="noopener" target="_blank" title="Visit gRPC">
				gRPC			</a>

		</h3>

					<span class="project-category">
				Remote Procedure Cal</span>

		<div class="project-icons">

						<a title="gRPC on Github"
				href="https://github.com/grpc"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="gRPC on DevStats"
				href="https://grpc.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="gRPC Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#grpc-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="gRPC on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/grpc"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="gRPC on Twitter"
				href="https://twitter.com/grpcio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="gRPC Blog"
				href="http://www.grpc.io/blog/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>



						<a title="gRPC on YouTube"
				href="https://www.youtube.com/channel/UCrnk1HWelWnYtF78YZX80fg"
				 rel="noopener" target="_blank"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a>

						<a title="gRPC on Gitter"
				href="https://gitter.im/grpc/grpc"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>Gitter</title>
 <g>
  <rect id="svg_1" fill="currentColor" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2" fill="#FFF">
   <path class="inner-color" stroke="null" id="svg_3" d="m189.043259,281.800446c0,-57.955597 0.307602,-115.911194 -0.242386,-173.857445c-0.121185,-12.687393 4.055099,-16.89167 16.621368,-16.602669c35.657059,0.820328 29.933289,-2.61953 30.007828,30.436691q0.354263,166.61409 0.0746,333.218887c0,17.339142 -0.083923,17.525604 -17.497665,17.404419c-32.646027,-0.233063 -28.814606,3.859314 -28.926483,-28.600311c-0.16777,-54.002991 -0.046585,-107.996582 -0.037262,-161.999573zm89.445694,-0.037354c0,-57.955551 0.326202,-115.911118 -0.242401,-173.857361c-0.130524,-12.706062 3.989868,-16.854401 16.556061,-16.565399c35.218964,0.811043 30.035858,-2.638161 30.091766,30.473999q0.298279,165.95224 0.065277,331.90451c0,18.662781 -0.065277,18.830627 -19.119659,18.690735c-31.378204,-0.24231 -27.164642,3.477173 -27.285828,-27.332336c-0.223785,-54.441193 -0.065216,-108.882294 -0.065216,-163.323456l0,0.009308zm-174.155746,-116.032303c0.009354,-41.716446 0.410202,-83.432915 -0.233025,-125.140034c-0.186455,-12.305187 4.092392,-15.912853 15.922165,-15.567947c35.228264,0.988171 30.641777,-4.204273 30.734978,31.024014c0.214432,78.156578 0.083923,156.313194 0.046616,234.479088c0,17.180664 -0.428802,17.609467 -17.805222,17.646729c-33.895218,0.065308 -28.376511,1.258514 -28.590942,-27.835815c-0.279648,-38.202026 -0.065216,-76.404022 -0.065216,-114.606033l-0.009354,0zm258.85643,33.485016c0.009308,-31.163803 0.251709,-62.336975 -0.130524,-93.500778c-0.121185,-9.900085 3.020355,-14.402679 13.51712,-14.272171c39.712128,0.475449 32.757904,-3.141533 32.990906,31.340942c0.382202,55.746262 0.121185,111.492477 0.093231,167.238693c-0.009308,17.767944 -0.251709,18.103577 -17.245972,18.131531c-33.997711,0.065277 -28.917084,1.883026 -29.178101,-28.618896c-0.233093,-26.763794 -0.046661,-53.546204 -0.046661,-80.319321z"/>
  </g>
 </g>
</svg></a>

		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://kubeedge.io/en/"  rel="noopener" target="_blank" title="KubeEdge (accepted to CNCF on 3/18/2019)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/kubeedge.svg" class="project-thumbnail" alt="" loading="lazy" height="356.51" width="364.26" />				</a>

		<h3 class="project-title">

					<a href="https://kubeedge.io/en/"  rel="noopener" target="_blank" title="Visit KubeEdge">
				KubeEdge			</a>

		</h3>

					<span class="project-category">
				Edge</span>

		<div class="project-icons">

						<a title="KubeEdge on Github"
				href="https://github.com/kubeedge/kubeedge"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="KubeEdge on DevStats"
				href="https://kubeedge.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="KubeEdge Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#kubeedge-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>


						<a title="KubeEdge on Twitter"
				href="https://twitter.com/KubeEdge"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>


						<a title="KubeEdge Contact"
				href="https://groups.google.com/forum/#!forum/kubeedge"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>

						<a title="KubeEdge Slack"
				href="https://kubeedge.slack.com/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://linkerd.io/"  rel="noopener" target="_blank" title="Linkerd (accepted to CNCF on 1/23/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/linkerd.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://linkerd.io/"  rel="noopener" target="_blank" title="Visit Linkerd">
				Linkerd			</a>

		</h3>

					<span class="project-category">
				Service Mesh</span>

		<div class="project-icons">

						<a title="Linkerd on Github"
				href="https://github.com/linkerd/linkerd"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Linkerd on DevStats"
				href="https://linkerd.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Linkerd Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#linkerd-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Linkerd on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/linkerd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Linkerd on Twitter"
				href="https://twitter.com/linkerd"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Linkerd Blog"
				href="https://blog.linkerd.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>


						<a title="Linkerd Slack"
				href="https://slack.linkerd.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>

						<a title="Linkerd on YouTube"
				href="https://www.youtube.com/watch?v=wBgBwNZo_EE&amp;list=PLI9FkLPXDscDB0gevkhEnyfgIfWF5yk4V"
				 rel="noopener" target="_blank"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a>


		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://nats.io/"  rel="noopener" target="_blank" title="NATS (accepted to CNCF on 3/15/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/nats.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://nats.io/"  rel="noopener" target="_blank" title="Visit NATS">
				NATS			</a>

		</h3>

					<span class="project-category">
				Messaging</span>

		<div class="project-icons">

						<a title="NATS on Github"
				href="https://github.com/nats-io"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="NATS on DevStats"
				href="https://nats.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="NATS Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#nats-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="NATS on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/nats.io"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="NATS on Twitter"
				href="https://twitter.com/nats_io"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="NATS Blog"
				href="https://nats.io/blog/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>


						<a title="NATS Slack"
				href="https://natsio.slack.com/join/shared_invite/enQtMzE2NDkxNDI2NTE1LTc5ZDEzYTkwYWZkYWQ5YjY1MzBjMWZmYzA5OGQxMzlkMGQzMjYxNGM3MWYxMjNiYmNjNzIwMTVjMWE2ZDgxZGM"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://github.com/theupdateframework/notary"  rel="noopener" target="_blank" title="Notary (accepted to CNCF on 10/24/2017)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/notary.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="https://github.com/theupdateframework/notary"  rel="noopener" target="_blank" title="Visit Notary">
				Notary			</a>

		</h3>

					<span class="project-category">
				Security</span>

		<div class="project-icons">

						<a title="Notary on Github"
				href="https://github.com/theupdateframework/notary"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Notary on DevStats"
				href="https://notary.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Notary Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#notary-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Notary on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/notary"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>







		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="http://www.openpolicyagent.org/"  rel="noopener" target="_blank" title="Open Policy Agent (accepted to CNCF on 3/29/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/opa.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="http://www.openpolicyagent.org/"  rel="noopener" target="_blank" title="Visit Open Policy Agent">
				Open Policy Agent			</a>

		</h3>

					<span class="project-category">
				Policy</span>

		<div class="project-icons">

						<a title="Open Policy Agent on Github"
				href="https://github.com/open-policy-agent/opa"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Open Policy Agent on DevStats"
				href="https://opa.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Open Policy Agent Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#opa-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="Open Policy Agent on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/open-policy-agent"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="Open Policy Agent on Twitter"
				href="https://twitter.com/openpolicyagent"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="Open Policy Agent Blog"
				href="https://blog.openpolicyagent.org/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>


						<a title="Open Policy Agent Slack"
				href="http://slack.openpolicyagent.org/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="http://opentracing.io/"  rel="noopener" target="_blank" title="OpenTracing (accepted to CNCF on 10/11/2016)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/05/open-tracing.svg" class="project-thumbnail" alt="" loading="lazy" height="100" width="100" />				</a>

		<h3 class="project-title">

					<a href="http://opentracing.io/"  rel="noopener" target="_blank" title="Visit OpenTracing">
				OpenTracing			</a>

		</h3>

					<span class="project-category">
				Distributed Tracing API</span>

		<div class="project-icons">

						<a title="OpenTracing on Github"
				href="https://github.com/opentracing"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="OpenTracing on DevStats"
				href="https://opentracing.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="OpenTracing Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/incubating.md#opentracing-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>

						<a title="OpenTracing on Stack Overflow"
				href="https://stackoverflow.com/questions/tagged/opentracing"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Stack Overflow" role="img"
viewbox="0 0 512 512"><title>Stack Overflow</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path stroke="#fff" class="inner-color" stroke-width="30" fill="none" d="M293 89l90 120zm-53 50l115 97zm-41 65l136 64zm-23 69l148 31zm-6 68h150zm-45-44v105h241V297"/></svg></a>

						<a title="OpenTracing on Twitter"
				href="https://twitter.com/opentracing"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="OpenTracing Blog"
				href="https://medium.com/opentracing"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="OpenTracing Contact"
				href="https://groups.google.com/forum/#!forum/opentracing"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>



						<a title="OpenTracing on Gitter"
				href="https://gitter.im/opentracing/public"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>Gitter</title>
 <g>
  <rect id="svg_1" fill="currentColor" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2" fill="#FFF">
   <path class="inner-color" stroke="null" id="svg_3" d="m189.043259,281.800446c0,-57.955597 0.307602,-115.911194 -0.242386,-173.857445c-0.121185,-12.687393 4.055099,-16.89167 16.621368,-16.602669c35.657059,0.820328 29.933289,-2.61953 30.007828,30.436691q0.354263,166.61409 0.0746,333.218887c0,17.339142 -0.083923,17.525604 -17.497665,17.404419c-32.646027,-0.233063 -28.814606,3.859314 -28.926483,-28.600311c-0.16777,-54.002991 -0.046585,-107.996582 -0.037262,-161.999573zm89.445694,-0.037354c0,-57.955551 0.326202,-115.911118 -0.242401,-173.857361c-0.130524,-12.706062 3.989868,-16.854401 16.556061,-16.565399c35.218964,0.811043 30.035858,-2.638161 30.091766,30.473999q0.298279,165.95224 0.065277,331.90451c0,18.662781 -0.065277,18.830627 -19.119659,18.690735c-31.378204,-0.24231 -27.164642,3.477173 -27.285828,-27.332336c-0.223785,-54.441193 -0.065216,-108.882294 -0.065216,-163.323456l0,0.009308zm-174.155746,-116.032303c0.009354,-41.716446 0.410202,-83.432915 -0.233025,-125.140034c-0.186455,-12.305187 4.092392,-15.912853 15.922165,-15.567947c35.228264,0.988171 30.641777,-4.204273 30.734978,31.024014c0.214432,78.156578 0.083923,156.313194 0.046616,234.479088c0,17.180664 -0.428802,17.609467 -17.805222,17.646729c-33.895218,0.065308 -28.376511,1.258514 -28.590942,-27.835815c-0.279648,-38.202026 -0.065216,-76.404022 -0.065216,-114.606033l-0.009354,0zm258.85643,33.485016c0.009308,-31.163803 0.251709,-62.336975 -0.130524,-93.500778c-0.121185,-9.900085 3.020355,-14.402679 13.51712,-14.272171c39.712128,0.475449 32.757904,-3.141533 32.990906,31.340942c0.382202,55.746262 0.121185,111.492477 0.093231,167.238693c-0.009308,17.767944 -0.251709,18.103577 -17.245972,18.131531c-33.997711,0.065277 -28.917084,1.883026 -29.178101,-28.618896c-0.233093,-26.763794 -0.046661,-53.546204 -0.046661,-80.319321z"/>
  </g>
 </g>
</svg></a>

		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://operatorframework.io/"  rel="noopener" target="_blank" title="Operator Framework (accepted to CNCF on 7/9/2020)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/operatorframework-icon-color.svg" class="project-thumbnail" alt="" loading="lazy" height="360.36" width="360.36" />				</a>

		<h3 class="project-title">

					<a href="https://operatorframework.io/"  rel="noopener" target="_blank" title="Visit Operator Framework">
				Operator Framework			</a>

		</h3>

					<span class="project-category">
				Operator Lifecycle Manager (OLM) + Operator SDK</span>

		<div class="project-icons">

						<a title="Operator Framework on Github"
				href="https://github.com/operator-framework/operator-sdk"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Operator Framework on DevStats"
				href="https://operatorframework.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>









		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://spiffe.io/"  rel="noopener" target="_blank" title="SPIFFE (accepted to CNCF on 3/29/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/spiffe.svg" class="project-thumbnail" alt="" loading="lazy" height="99.58" width="99.58" />				</a>

		<h3 class="project-title">

					<a href="https://spiffe.io/"  rel="noopener" target="_blank" title="Visit SPIFFE">
				SPIFFE			</a>

		</h3>

					<span class="project-category">
				Identity Spec</span>

		<div class="project-icons">

						<a title="SPIFFE on Github"
				href="https://github.com/spiffe"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="SPIFFE on DevStats"
				href="https://spiffe.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="SPIFFE Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#spiffe-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>


						<a title="SPIFFE on Twitter"
				href="https://twitter.com/spiffeio"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>

						<a title="SPIFFE Blog"
				href="https://blog.spiffe.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-0.48 -0.48 24.86 24.86" aria-labelledby="rss-title"><title id="rss-title">RSS Feed</title><path class="inner-color" d="M19 0H5C2.239 0 0 2.239 0 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5V5c0-2.761-2.238-5-5-5zM6.168 20C4.971 20 4 19.031 4 17.835s.971-2.165 2.168-2.165 2.167.969 2.167 2.165S7.365 20 6.168 20zm5.18 0c-.041-4.029-3.314-7.298-7.348-7.339V9.454C9.814 9.495 14.518 14.193 14.561 20zm5.441 0C16.768 12.937 11.053 7.239 4 7.208V4c8.83.031 15.98 7.179 16 16z"/></svg></a>

						<a title="SPIFFE Contact"
				href="https://groups.google.com/a/spiffe.io/forum/#!forum/announce"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a>

						<a title="SPIFFE Slack"
				href="https://slack.spiffe.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://github.com/spiffe/spire"  rel="noopener" target="_blank" title="SPIRE (accepted to CNCF on 3/29/2018)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/spire.svg" class="project-thumbnail" alt="" loading="lazy" height="102.31" width="75.44" />				</a>

		<h3 class="project-title">

					<a href="https://github.com/spiffe/spire"  rel="noopener" target="_blank" title="Visit SPIRE">
				SPIRE			</a>

		</h3>

					<span class="project-category">
				Identity</span>

		<div class="project-icons">

						<a title="SPIRE on Github"
				href="https://github.com/spiffe/spire"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="SPIRE on DevStats"
				href="https://spire.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="SPIRE Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#spire-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>








		</div>

	</div>
				<div class="project-box">
		<!-- thumbnail  -->
							<a href="https://thanos.io/"  rel="noopener" target="_blank" title="Thanos (accepted to CNCF on 7/20/2019)">
				<img src="https://www.cncf.io/wp-content/uploads/2020/08/thanos-icon.svg" class="project-thumbnail" alt="" loading="lazy" height="355.17" width="355.42" />				</a>

		<h3 class="project-title">

					<a href="https://thanos.io/"  rel="noopener" target="_blank" title="Visit Thanos">
				Thanos			</a>

		</h3>

					<span class="project-category">
				Monitoring</span>

		<div class="project-icons">

						<a title="Thanos on Github"
				href="https://github.com/thanos-io"
				 rel="noopener" target="_blank"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a>

						<a title="Thanos on DevStats"
				href="https://thanos.devstats.cncf.io/"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" role="img" viewbox="-10.23 -10.23 531.96 531.96"><title>DevStats</title><path fill="none" d="M-1-1h582v402H-1z"/><rect width="512" height="512" rx="15%"/><path fill="#FFF" d="M285.9 116c.1 1.8.30001 3.7.30001 5.5v136.29999c0 6.6 0 6.6-6.40002 6.70001-11.79999 0-23.59998-.1-35.4 0-3.3 0-4.8-.9-4.8-4.6.1-47.1.1-94.3.1-141.4 0-.79999.2-1.69999.2-2.5h46zm-56.8 91.6v51.10001c0 5.79999 0 5.79999-5.60002 5.79999-12.09999 0-24.09999-.09998-36.2.1-3.8.10001-4.89999-1.29998-4.89999-5 .1-34.59999.1-69.3 0-103.9 0-3.6 1-5.1 4.8-5 12.3.2 24.7.2 37 0 3.8-.1 4.9 1.3 4.8 5 0 17.3.1 34.6.1 51.9zM172 223c0 12.2-.1 24.4.1 36.6.1 3.70002-1.1 5-4.9 4.9-12.3-.19998-24.7-.19998-37 0-3.8.1-4.8-1.4-4.8-5 .1-24.4.1-48.8 0-73.2 0-3.5 1.2-4.8 4.7-4.8 12.5.1 25 .1 37.4 0 3.6 0 4.6 1.4 4.6 4.8-.2 12.3-.1 24.5-.1 36.7z"/><path fill="#FFF" stroke="null" d="M44.9 443.5v-6.29999c9.5-27.80002 19.4-55.5 28.2-83.5C76.1 344.4 80.6 341.3 90.3 341.4c109.9.30002 219.8.30002 329.7 0 9.70001 0 14.30002 3 17.20001 12.30002 8.9 28 18.8 55.69998 28.3 83.5V443.5c-4.2.29999-8.3.79999-12.5.79999H57.4c-4.2 0-8.4-.5-12.5-.79999zM256.20001 55.7h154.5C427.8 55.7 433.9 61.2 433.9 78.1c.20002 74.6.20002 149.3 0 223.9 0 16.9-6.1 22.4-23.29998 22.4H99.4C82.3 324.4 76.2 318.79998 76.2 302c-.2-74.6-.2-149.30002 0-223.9 0-16.8 6.2-22.3 23.3-22.3 52.3-.2 104.5-.1 156.70001-.1zm-1.1 242.2h145.1C413.9 297.9 414.4 297.4 414.4 283.7V96.5c0-13.8-.69998-14.6-14-14.6H110.2C96.7 81.9 96 82.7 96 96.3v187.2c0 14.1.3 14.4 15.1 14.4h144z"/></svg></a>

						<a title="Thanos Logos"
				href="https://github.com/cncf/artwork/blob/master/examples/sandbox.md#thanos-logos"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewbox="0 0 512 512"><title>LF Artwork</title>
 <g>
  <rect id="svg_1" width="512" rx="15%" height="512"/>
  <g stroke="null" id="svg_2">
   <path stroke="null" id="svg_3" d="m112.19075,327.609558l-54.519749,0l0,127.057007l127.057011,0l0,-54.414276l-72.537262,0l0,-72.642731z" fill="#FFF"/>
   <path stroke="null" id="svg_4" d="m384.337433,328.016602l0,72.235687l-72.235779,0l-0.301544,-0.407074l0,54.82135l126.951508,0l0,-127.057007l-54.82135,0l0.407166,0.407043z" fill="#FFF"/>
   <path stroke="null" id="svg_5" d="m57.671001,200.642944l54.926846,0l-0.407097,-0.407089l0,-72.235703l72.130173,0l0.407089,0.407089l0,-54.821365l-127.057011,0l0,127.057068z" fill="#FFF"/>
   <g stroke="null" id="svg_6" fill="#FFF" opacity="0.6">
    <path stroke="null" id="svg_7" d="m232.417725,128.000153l37.256287,0l56.163177,-54.414276l-141.109177,0l0,54.821365"/>
    <path stroke="null" id="svg_8" d="m264.004852,400.252289l-24.862564,0l-54.414276,0l0,54.414276l127.072098,0l0,-54.82135"/>
    <path stroke="null" id="svg_9" d="m383.930267,327.609558l54.82135,0l0,-155.04068l-54.414185,56.163208l0,26.325073l0,24.86261"/>
    <path stroke="null" id="svg_10" d="m112.597847,200.642944l-54.926846,0l0,126.966614l54.519749,0l0,-79.276901"/>
   </g>
   <g stroke="null" id="svg_11" fill="#FFF">
    <path stroke="null" id="svg_12" d="m150.309402,357.421234c1.21962,-3.879547 1.801163,-7.902313 2.62587,-11.868134q8.718338,-41.920654 17.366272,-83.855988c0.517761,-2.501831 1.045456,-5.001617 1.596512,-7.636246c0.233292,0.245941 0.381165,0.340332 0.44133,0.474228a22.587265,22.587265 0 0 0 18.646957,12.947327a28.667822,28.667822 0 0 0 4.766266,0.384949c1.286575,-0.007874 1.519226,0.387787 1.398544,1.63501a41.005035,41.005035 0 0 0 3.094238,20.670013a33.577316,33.577316 0 0 0 24.058777,19.304138a64.830452,64.830452 0 0 0 14.879578,1.845062c0.810684,0.018402 1.390274,-0.012939 1.433517,1.18103a20.126488,20.126488 0 0 0 16.332138,20.09024c0.359314,0.09726 0.78595,0.022675 1.149231,0.575043c-3.976242,0.931519 -7.883209,1.849701 -11.79158,2.761902q-47.393326,11.061981 -94.787399,22.120758c-0.314209,0.073486 -0.670532,0.037598 -0.879761,0.361877c-0.709122,-0.130432 -0.169159,-0.678345 -0.33049,-0.991211z"/>
    <path stroke="null" id="svg_13" d="m235.04332,295.209625a23.74777,23.74777 0 0 1 -21.996338,-14.465424a23.199253,23.199253 0 0 1 4.834076,-25.397964c9.058472,-9.171738 18.211807,-18.25 27.327164,-27.365479q64.976196,-64.978043 129.925598,-129.982025c1.161011,-1.16349 1.70697,-1.189888 2.878326,-0.005867q15.227386,15.389793 30.608887,30.627403c0.94339,0.936768 1.047119,1.395737 0.042694,2.398987q-78.573669,78.489212 -157.084152,157.042328a23.587801,23.587801 0 0 1 -16.536255,7.148041z"/>
    <path stroke="null" id="svg_14" d="m474.283417,106.635506a32.31971,32.31971 0 0 1 -9.132446,21.638481c-5.465729,5.744476 -11.199341,11.23262 -16.752533,16.894806c-1.109833,1.131668 -1.486328,0.096451 -2.022308,-0.438904q-26.303955,-26.273712 -52.585205,-52.568649q-15.891571,-15.890533 -31.799408,-31.762486c-0.87735,-0.872513 -1.023315,-1.347591 -0.050781,-2.29821c5.198761,-5.081848 10.28891,-10.274502 15.469391,-15.374702a33.88203,33.88203 0 0 1 48.589722,0.078999q19.107849,18.980732 38.091278,38.086784a34.610722,34.610722 0 0 1 10.192291,25.743881z"/>
    <path stroke="null" id="svg_15" d="m197.66333,251.049179a11.679537,11.679537 0 0 1 -10.206604,-7.38356a12.132613,12.132613 0 0 1 2.123367,-13.686478c0.286484,-0.334106 0.597931,-0.6474 0.909439,-0.958786q78.706146,-78.694717 157.415192,-157.386383c0.272461,-0.272453 0.583496,-0.510681 0.830353,-0.80378c0.748871,-0.888794 1.326019,-0.738792 2.12088,0.067116q7.834381,7.937157 15.774292,15.769691c0.717682,0.708649 0.799072,1.203979 0.069305,1.873863c-0.445374,0.40905 -0.838287,0.874466 -1.266479,1.302666q-78.348541,78.351234 -156.686768,156.712425a14.174545,14.174545 0 0 1 -11.082977,4.493225z"/>
    <path stroke="null" id="svg_16" d="m255.017853,307.091309a12.28007,12.28007 0 0 1 3.338562,-8.555511c0.444672,-0.488464 0.914612,-0.954529 1.381866,-1.421906q78.1745,-78.188385 156.350403,-156.375183c2.302765,-2.30304 2.30368,-2.303329 4.55835,-0.049469c4.831268,4.82959 9.638824,9.683334 14.51413,14.467941c0.878021,0.862045 0.982697,1.45813 0.046692,2.242645c-0.377991,0.31662 -0.696381,0.704575 -1.046936,1.05542q-78.415833,78.417435 -156.821014,156.844528a12.672233,12.672233 0 0 1 -14.434448,3.506958a12.331936,12.331936 0 0 1 -7.887604,-11.715424z"/>
   </g>
  </g>
 </g>
</svg></a>


						<a title="Thanos on Twitter"
				href="https://twitter.com/ThanosMetrics"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg></a>



						<a title="Thanos Slack"
				href="https://cloud-native.slack.com/messages/CK5RSSC10"
				 rel="noopener" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a>



		</div>

	</div>
			</div>




<div style="height:39px" aria-hidden="true" class="wp-block-spacer"></div>



<h3>Maturity levels</h3>



<p>CNCF projects have a maturity level of sandbox, incubating, or graduated, which corresponds to the Innovators, Early Adopters, and Early Majority tiers of the Crossing the Chasm diagram. The maturity level is a signal by CNCF as to what sorts of enterprises should be adopting different projects. Projects increase their maturity by demonstrating their sustainability to CNCF’s Technical Oversight Committee: that they have adoption, a healthy rate of changes, and committers from multiple organizations; have adopted the CNCF&nbsp;<a href="https://github.com/cncf/foundation/blob/master/code-of-conduct.md">Code of Conduct</a>; and have achieved and maintained the Core Infrastructure Initiative&nbsp;<a href="https://bestpractices.coreinfrastructure.org/">Best Practices Badge</a>. Full details are in the&nbsp;<a href="https://github.com/cncf/toc/blob/master/process/graduation_criteria.adoc">Graduation Criteria v1.1</a>.</p>



<figure class="wp-block-image size-large"><img loading="lazy" width="2561" height="977" src="https://www.cncf.io/wp-content/uploads/2020/07/graphic-chasm-3-02.svg" alt="" class="wp-image-39297"/></figure>



<p><a rel="noreferrer noopener" href="https://github.com/cncf/toc/blob/master/process/project_proposals.adoc" target="_blank">View the project proposal process</a>.</p>
	</article>
</main>

<footer class="footer">
	<div class="container wrap">

	<section class="newsletter" id="newsletter">
	<h3>Subscribe to the CNCF newsletter to receive regular updates about
		webinars, events & latest news</h3>

	<form id="sfmc-form1" class="newsletter-form"
		action="https://cloud.email.thelinuxfoundation.org/CNCF-Newsletter-Subscriber-Form">
		<label for="FirstName" required>
		<span class="screen-reader-text">First Name</span>
			<input type="text" id="FirstName" name="FirstName" placeholder="First Name" autocomplete="given-name" spellcheck="false"
				required>
		</label>
		<label for="LastName" required>
		<span class="screen-reader-text">Last Name</span>
			<input type="text" id="LastName" name="LastName" placeholder="Last Name" autocomplete="family-name" spellcheck="false"
				required>
		</label>
		<label for="EmailAddress" required>
		<span class="screen-reader-text">Email Address</span>
			<input type="email" id="EmailAddress" name="EmailAddress"
				placeholder="Email Address" autocomplete="email" spellcheck="false" required>
		</label>
		<label for="Language" required>
		<span class="screen-reader-text">Language</span>
			<select id="Language" name="Language" class="form-control select-css newsletter-select" required onchange="this.dataset.selected = this.value;">
			<option value="" disabled>Language</option>
				<option value="English">English</option>
				<option value="Chinese">中文</option>
			</select>
		</label>
		<button type="submit" class="button"
		id="sfmc-submit1">Subscribe</button>
		<div id="recaptcha-form1" style="display:none;"></div>
	</form>
	<div id="sfmc-message1" class="form-message"></div>
	<p class="privacy-agreement">By submitting this form, you acknowledge that
	your
		information is subject to The Linux Foundation’s <a
			href="https://www.linuxfoundation.org/privacy/"
			rel="noopener" class="external"
			target="_blank">Privacy Policy</a>.</p>
</section>

	<div class="copyright-text">
				<p>Copyright &copy; 2020					The Linux Foundation®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our <a href="https://www.linuxfoundation.org/trademark-usage" target="_blank" rel="noopener">Trademark Usage</a> page. Linux is a registered trademark of Linus Torvalds. <a href="https://www.linuxfoundation.org/privacy" target="_blank" rel="noopener">Privacy Policy</a> and <a href="https://www.linuxfoundation.org/terms" target="_blank" rel="noopener">Terms of Use</a>. Forms on this site are protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener">Terms of Service</a> apply.				</p>
			</div>


<ul class="social-links">
		<li class="social_twitter"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on Twitter"
			href="https://twitter.com/cloudnativefdn"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitter" role="img"
viewbox="0 0 512 512"><title>Twitter</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path class="inner-color" fill="#fff" d="M437 152a72 72 0 0 1-40 12 72 72 0 0 0 32-40 72 72 0 0 1-45 17 72 72 0 0 0-122 65 200 200 0 0 1-145-74 72 72 0 0 0 22 94 72 72 0 0 1-32-7 72 72 0 0 0 56 69 72 72 0 0 1-32 1 72 72 0 0 0 67 50 200 200 0 0 1-105 29 200 200 0 0 0 309-179 200 200 0 0 0 35-37"/></svg>		</a></li>

		<li class="social_wechat_id"><button class="js-modal button-reset" data-modal-content-id="modal-wechat" data-modal-prefix-class="lf" data-modal-close-text="Close" title="Cloud Native Computing Foundation on WeChat"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="WeChat" role="img"
viewbox="0 0 512 512"
fill="#fff"><title>WeChat</title><rect
width="512" height="512"
rx="15%"
fill="currentColor" /><path class="inner-color" fill="#FFF" d="m402 369c23-17 38-42 38-70 0-51-50-92-111-92s-110 41-110 92 49 92 110 92c13 0 25-2 36-5 4-1 8 0 9 1l25 14c3 2 6 0 5-4l-6-22c0-3 2-5 4-6m-110-85a15 15 0 1 1 0-29 15 15 0 0 1 0 29m74 0a15 15 0 1 1 0-29 15 15 0 0 1 0 29"/><path class="inner-color" fill="#FFF" d="m205 105c-73 0-132 50-132 111 0 33 17 63 45 83 3 2 5 5 4 10l-7 24c-1 5 3 7 6 6l30-17c3-2 7-3 11-2 26 8 48 6 51 6-24-84 59-132 123-128-10-52-65-93-131-93m-44 93a18 18 0 1 1 0-35 18 18 0 0 1 0 35m89 0a18 18 0 1 1 0-35 18 18 0 0 1 0 35"/></svg></button></li>


		<li class="social_youtube"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on YouTube"
			href="https://www.youtube.com/c/cloudnativefdn"><svg fill="currentColor" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>YouTube</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m427 169c-4-15-17-27-32-31-34-9-239-10-278 0-15 4-28 16-32 31-9 38-10 135 0 174 4 15 17 27 32 31 36 10 241 10 278 0 15-4 28-16 32-31 9-36 9-137 0-174" fill="#FFF" /><path d="m220 203v106l93-53"/></svg></a></li>

		<li class="social_github"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on Github"
			href="https://github.com/cncf"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Github</title><rect height="512" rx="15%" width="512" fill="currentColor"/><path class="inner-color" d="m335 499c14 0 12 17 12 17h-182s-2-17 12-17c13 0 16-6 16-12l-1-50c-71 16-86-28-86-28-12-30-28-37-28-37-24-16 1-16 1-16 26 2 40 26 40 26 22 39 59 28 74 22 2-17 9-28 16-35-57-6-116-28-116-126 0-28 10-51 26-69-3-6-11-32 3-67 0 0 21-7 70 26 42-12 86-12 128 0 49-33 70-26 70-26 14 35 6 61 3 67 16 18 26 41 26 69 0 98-60 120-117 126 10 8 18 24 18 48l-1 70c0 6 3 12 16 12z" fill="#fff"/></svg></a></li>

		<li class="social_flickr"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on Flickr"
			href="https://www.flickr.com/photos/143247548@N03/albums/with/72157676361993185"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Flickr</title><rect height="512" rx="15%" width="512"/><circle class="inner-color slight-shadow" cx="157" cy="256" fill="#f9f9f9" r="93"/><circle class="inner-color" cx="355" cy="256" fill="#FFF" r="93"/></svg></a></li>

		<li class="social_linkedin"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on LinkedIn"
			href="https://www.linkedin.com/company/cloud-native-computing-foundation/"><svg xmlns="http://www.w3.org/2000/svg" aria-label="LinkedIn" role="img" viewbox="0 0 512 512" fill="currentColor"><title>LinkedIn</title>
<rect width="512" height="512" rx="15%" fill="currentColor" />
<circle cx="142" cy="138" r="37" fill="#FFF" class="inner-color"/>
<path stroke="#FFF" stroke-width="66" d="M244 194v198M142 194v198" class="inner-color"/>
<path fill="#FFF" d="M276 282c0-20 13-40 36-40 24 0 33 18 33 45v105h66V279c0-61-32-89-76-89-34 0-51 19-59 32" class="inner-color"/>
</svg>

</a></li>

		<li class="social_email"><a title="Contact Cloud Native Computing Foundation"
			href="https://www.cncf.io/about/contact/"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-labelledby="email-title"><title id="email-title">Email Icon</title><rect height="512" rx="15%" width="512"/><rect fill="#fff" class="inner-color" height="256" rx="8%" width="356" x="78" y="128"/><path d="m434 128-165 164c-7 8-19 8-26 0l-165-164m0 256 129-128m227 128-129-128" fill="none" stroke="currentColor" stroke-width="20"/></svg></a></li>

		<li class="social_facebook"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on Facebook"
			href="https://www.facebook.com/CloudNativeComputingFoundation/"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Facebook" role="img"
viewbox="0 0 512 512" aria-labelledby="fb-title"><title id="fb-title">Facebook Icon</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path fill="#FFF" class="inner-color" d="M355.6 330l11.4-74h-71v-48c0-20.2 9.9-40 41.7-40H370v-63s-29.3-5-57.3-5c-58.5 0-96.7 35.4-96.7 99.6V256h-65v74h65v182h80V330h59.6z" /></svg></a></li>


		<li class="social_meetup"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on Meetup"
			href="http://www.meetup.com/pro/cncf/"><svg viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><title>Meetup</title><rect height="512" rx="15%" width="512"/><path class="inner-color" d="m335 138c6 1 21-16 54-7 57 17 11 98 4 113-10 19-53 101-13 109 18 4 46 0 42 26-3 27-65 13-77 7-52-22-39-77-14-118 10-21 45-70 23-78-14-5-29 34-34 45-6 12-44 86-52 98-20 32-57 16-49-11 11-35 56-116 29-120-14-2-21 14-25 23-8 16-38 102-53 134-19 40-99 23-85-37 5-23 34-113 40-129 12-30 24-69 70-70 13 0 33 15 47 20 14 4 24-24 50-26 32-2 31 20 43 21z" fill="#fff"/></svg></a></li>

		<li class="social_slack"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation Slack"
			href="https://slack.cncf.io/"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
aria-label="Slack" role="img"
viewbox="0 0 512 512"><title>Slack</title><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><g fill="#FFF" class="inner-color"><path id="a" d="M149 305a39 39 0 0 1-78 0c0-22 17-39 39-39h39zM168 305a39 39 0 0 1 78 0v97a39 39 0 0 1-78 0z"/></g><use xlink:href="#a" class="inner-color"  fill="#FFF" transform="rotate(90,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color" transform="rotate(180,256,256)"/><use xlink:href="#a" fill="#FFF" class="inner-color"  transform="rotate(270,256,256)"/></svg></a></li>

		<li class="social_twitch"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation on Twitch"
			href="https://www.twitch.tv/cloudnativefdn"><svg xmlns="http://www.w3.org/2000/svg"
aria-label="Twitch" role="img"
viewbox="0 0 512 512"><rect
width="512" height="512"
rx="15%"
fill="currentColor"/><path fill="#fff" class="inner-color" d="m115 101-22 56v228h78v42h44l41-42h63l85-85v-199zm260 185-48 48h-78l-42 42v-42h-65v-204h233zm-48-100v85h-30v-85zm-78 0v85h-29v-85z"/></svg></a></li>

		<li class="social_rss"><a target="_blank" rel="noopener" title="Cloud Native Computing Foundation RSS feed"
			href="https://www.cncf.io/feed"><svg height="500" width="500" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 50 50" fill="currentColor"><title>RSS</title><path d="M45 1H5C2.8 1 1 2.8 1 5v40c0 2.2 1.8 4 4 4h40c2.2 0 4-1.8 4-4V5c0-2.2-1.8-4-4-4z" fill="currentColor"/><circle cx="15.5" cy="34.5" fill="#FFF" class="inner-color"  r="3.5"/><path d="M12 12v4.3c12 0 21.7 9.7 21.7 21.7H38c0-14.4-11.6-26-26-26z" class="inner-color" fill="#FFF"/><path d="M12 20.7V25c7.2 0 13 5.8 13 13h4.3c0-9.6-7.7-17.3-17.3-17.3z" class="inner-color" fill="#FFF"/></svg></a></li>
	</ul>

	<!-- Modal -->
	<div class="modal-hide" id="modal-wechat" aria-hidden="true">
			<div class="modal-content-wrapper">
				<div class="modal__content"
					id="modal-wechat-content">
					<img loading="lazy" src="https://www.cncf.io/wp-content/uploads/2020/05/wechat-qrcode-cncf.png">
				</div>
			</div>
		</div>

	</div>
</footer>

<div class="back-to-top vanillatop">
	<span title="Go to top" name="Go to top of page"
		aria-label="Go to top of page">
		<svg aria-hidden="true" data-prefix="fas" data-icon="chevron-up" role="img" xmlns="http://www.w3.org/2000/svg" viewbox="0 0 448 512" class="fa-chevron-up" aria-labelledby="chevron-title"><title id="chevron-title">Go to Top Chevron Up</title><path fill="currentColor" d="M240.971 130.524l194.343 194.343c9.373 9.373 9.373 24.569 0 33.941l-22.667 22.667c-9.357 9.357-24.522 9.375-33.901.04L224 227.495 69.255 381.516c-9.379 9.335-24.544 9.317-33.901-.04l-22.667-22.667c-9.373-9.373-9.373-24.569 0-33.941L207.03 130.525c9.372-9.373 24.568-9.373 33.941-.001z"></path></svg>	</span>
</div>


<div id="cookie-banner">This website uses cookies to offer you a better browsing experience<a target="_blank" class="external cookie-link" rel="noopener" href="https://www.linuxfoundation.org/cookies/">Find out more about how we use cookies and how you can change your settings</a>	<button
		id="cookie-banner-button" tabindex="0" role="button">
		<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
			viewbox="0 0 24 24" fill="currentColor">
			<path
				d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-1.959 17l-4.5-4.319 1.395-1.435 3.08 2.937 7.021-7.183 1.422 1.409-8.418 8.591z" />
			</svg>
		Accept</button></div>

<div id="um_upload_single" style="display:none"></div>
<div id="um_view_photo" style="display:none">

	<a href="javascript:void(0);" data-action="um_remove_modal" class="um-modal-close"
	   aria-label="Close view photo modal">
		<i class="um-faicon-times"></i>
	</a>

	<div class="um-modal-body photo">
		<div class="um-modal-photo"></div>
	</div>

</div><script type='text/javascript' defer id='recaptcha-js' data-type="lazy" data-src="https://www.recaptcha.net/recaptcha/api.js?render=explicit&#038;ver=5.5.3"></script>
<script type='text/javascript' src='https://www.cncf.io/wp-content/themes/lf-theme/source/js/third-party/jquery-3.5.1.min.js?ver=3.5.1' id='jquery-js'></script>
<script type='text/javascript' id='sfmc-forms-js-extra' data-type="lazy" data-src="data:text/javascript;base64,Ci8qIDwhW0NEQVRBWyAqLwp2YXIgbGZfbXVfb2JqZWN0ID0geyJyZWNhcHRjaGFfa2V5IjoiNkxkTWxkVVVBQUFBQUJHMnZyWjFHVDdFb19UZ0ktVVBsRzE0b2NWSCJ9OwovKiBdXT4gKi8K"></script>
<script type='text/javascript' defer id='sfmc-forms-js' data-type="lazy" data-src="https://www.cncf.io/wp-content/mu-plugins/wp-mu-plugins/lf-mu/public/js/sfmc-forms.js?ver=1.0.0"></script>
<script type='text/javascript' id='flying-pages-js-before'>
window.FPConfig= {
	delay: 0,
	ignoreKeywords: ["\/wp-admin","\/wp-login.php","\/cart","add-to-cart","logout","#","?",".png",".jpeg",".jpg",".gif",".svg"],
	maxRPS: 3,
    hoverDelay: 50
};
</script>
<script type='text/javascript' defer src='https://www.cncf.io/wp-content/plugins/flying-pages/flying-pages.min.js?ver=2.4.2' id='flying-pages-js'></script>
<script type='text/javascript' defer src='https://www.cncf.io/wp-content/themes/lf-theme/build/global.min.js?ver=1605136055' id='global-scripts-js'></script>
<script type="text/javascript" id="flying-scripts">const loadScriptsTimer=setTimeout(loadScripts,5*1000);const userInteractionEvents=["mouseover","keydown","touchmove","touchstart"];userInteractionEvents.forEach(function(event){window.addEventListener(event,triggerScriptLoader,{passive:!0})});function triggerScriptLoader(){loadScripts();clearTimeout(loadScriptsTimer);userInteractionEvents.forEach(function(event){window.removeEventListener(event,triggerScriptLoader,{passive:!0})})}
function loadScripts(){document.querySelectorAll("script[data-type='lazy']").forEach(function(elem){elem.setAttribute("src",elem.getAttribute("data-src"))})}</script>
    		<script type="text/javascript">
			jQuery( window ).on( 'load', function() {
				jQuery('input[name="um_request"]').val('');
			});
		</script>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"NRJS-97e2229449e282c1bef","applicationID":"643908501","transactionName":"MVFSYxFWXhICUxdaXggbcVQXXl8PTEACVFQ=","queueTime":0,"applicationTime":943,"atts":"HRZRFVlMTRw=","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
</html>
    '''
    links = re.compile(r'<a title="(.*) on Github"\n.*href="(.*)"').findall(html)

    # gRPC, NATS, OpenTracing
    address = {
        "Harbor": "https://github.com/goharbor/harbor-operator",
        "Kubernetes": "https://github.com/kubernetes/kubernetes",
        "Prometheus": "https://github.com/prometheus/prometheus",
        "Argo": "https://github.com/argoproj/argo",
        "CNI": "https://github.com/containernetworking/cni",
        "gRPC": "https://github.com/grpc/grpc-go",
        "NATS": "https://github.com/nats-io/nats-server",
        "OpenTracing": "https://github.com/opentracing/opentracing-go",
        "SPIFFE": "https://github.com/spiffe/spire",
        "Thanos": "https://github.com/thanos-io/thanos"
    }

    graduated, incubating = [], []
    for i in range(33):
        link = links[i][1] if links[i][0] not in address else address[links[i][0]]
        link = link[len("https://github.com/"):]
        if link[-1] == '/':
            link = link[:-1]
        proj = {
            "project": links[i][0],
            "address": link
        }
        if i < 13:
            graduated.append(proj)
        else:
            incubating.append(proj)

    return graduated, incubating

