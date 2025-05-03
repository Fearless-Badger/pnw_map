<script setup>
import Navbar from './components/Navbar.vue';
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <Navbar />
    <router-view />
  </div>
</template>