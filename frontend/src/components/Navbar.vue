
<template>

    <nav class="navbar">
      <div class="container">
        <div class = "logo">
         <a href="#">PNW Events</a>
       </div>
    
       <ul :class="['links', {open: isOpen }]">
        <li> <RouterLink to="/events">Events</RouterLink></li>
        <li> <RouterLink to="/register">Register</RouterLink></li>
        <li> <RouterLink to="/signup">Sign Up</RouterLink></li>
        <li> <RouterLink to="/login">Log in</RouterLink></li>
       </ul> 
      </div>
    </nav>
    
    </template>
    
    <script setup>
    import { ref } from 'vue'
    
    const isOpen = ref(false)
    
    const toggleMenu = () => {
      isOpen.value = !isOpen.value
    }
    </script>
    
    <style scoped>
    
      .navbar{
        background-color: var(--pnw-white);
        border-bottom: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        position: relative;
      }
      .container{
        max-width: 1200px;
        padding: 0 1rem;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 60px;
      }
      .logo a{
        font-size: 1.5rem;
        font-weight: bold;
        color: var(--pnw-gold)
        }
        .links {
          list-style: none;
          display: flex;
          gap: 1.5rem;
        }
        .links li a {
          text-decoration: none;
          color: #333;
          font-weight: 500;
        }
        .links li a:hover {
          color: #0077cc;
        }
    </style>