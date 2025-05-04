<template>
  <nav class="navbar">
    <div class="nav-container">
      <router-link to="/" class="nav-brand">PNW Map</router-link>
      <div class="nav-links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/events" class="nav-link">Events</router-link>
        <router-link to="/signup" class="nav-link">Add Event</router-link>
        <template v-if="!auth.isLoggedIn.value">
          <router-link to="/login" class="nav-link">Login</router-link>
          <router-link to="/register" class="nav-link">Register</router-link>
        </template>
        <template v-else>
          <router-link to="/profile" class="nav-link">Profile</router-link>
          <button @click="handleLogout" class="nav-link logout-button">Logout</button>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { inject } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const auth = inject('auth')

const handleLogout = async () => {
  auth.logout()
  // Wait for the next tick to ensure the auth state is updated
  await router.push('/login')
}
</script>

<style scoped>
.navbar {
  background-color: var(--pnw-black);
  padding: 1rem 0;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand {
  color: var(--pnw-gold);
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-brand:hover {
  color: #bfa32f;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  flex-wrap: wrap;
}

.nav-link {
  color: var(--pnw-white);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.3s ease;
  font-weight: 500;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: var(--pnw-gold);
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-link:hover {
  color: var(--pnw-gold);
}

.nav-link:hover::after {
  width: 100%;
}

.logout-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  color: var(--pnw-white);
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  transition: all 0.3s ease;
  font-weight: 500;
  position: relative;
}

.logout-button::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background-color: #dc3545;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.logout-button:hover {
  color: #dc3545;
}

.logout-button:hover::after {
  width: 100%;
}

@media (max-width: 768px) {
  .nav-container {
    flex-direction: column;
    gap: 1rem;
  }

  .nav-links {
    width: 100%;
    justify-content: center;
  }
}
</style>