# Firebase (script que da)
```html
<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/12.18.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.18.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBBIOpWUjx-_zNfGRtTYZr196RkB_PIQYw",
    authDomain: "igcse-site.firebaseapp.com",
    projectId: "igcse-site",
    storageBucket: "igcse-site.firebasestorage.app",
    messagingSenderId: "449005094015",
    appId: "1:449005094015:web:27fca45ae270721004ab4a",
    measurementId: "G-KFVRJ0V0HL"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>
```