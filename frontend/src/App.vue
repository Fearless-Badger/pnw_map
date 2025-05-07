<script setup>
import { ref, provide, onMounted } from 'vue'
import NavBar from './components/Navbar.vue'

// Create reactive auth state
const isLoggedIn = ref(false)
const user = ref(null)

// Function to check login status
const checkLoginStatus = () => {
  console.log('=== CHECKING LOGIN STATUS ===')
  const storedUser = localStorage.getItem('user')
  console.log('Stored user:', storedUser)
  
  if (storedUser) {
    try {
      user.value = JSON.parse(storedUser)
      isLoggedIn.value = true
      console.log('User logged in:', user.value)
    } catch (error) {
      console.error('Error parsing user data:', error)
      localStorage.removeItem('user')
      user.value = null
      isLoggedIn.value = false
    }
  } else {
    console.log('No stored user found')
    user.value = null
    isLoggedIn.value = false
  }
  console.log('Current isLoggedIn value:', isLoggedIn.value)
}

// Function to login
const login = (userData) => {
  console.log('=== LOGGING IN USER ===')
  console.log('User data:', userData)
  user.value = userData
  isLoggedIn.value = true
  localStorage.setItem('user', JSON.stringify(userData))
  console.log('Updated isLoggedIn value:', isLoggedIn.value)
}

// Function to logout
const logout = () => {
  console.log('=== LOGGING OUT USER ===')
  // Clear localStorage first
  localStorage.removeItem('user')
  // Then update the reactive state
  user.value = null
  isLoggedIn.value = false
  console.log('Updated isLoggedIn value:', isLoggedIn.value)
}

// Provide auth state and methods to all components
const auth = {
  isLoggedIn,
  user,
  login,
  logout,
  checkLoginStatus
}

// Check login status before providing auth
checkLoginStatus()
provide('auth', auth)

onMounted(() => {
  console.log('=== APP MOUNTED ===')
  console.log('Initial auth state:', {
    isLoggedIn: isLoggedIn.value,
    user: user.value
  })
})
</script>

<template>
  <div class="app-container">
    <NavBar />
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<style>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 2rem;
  margin-top: 4rem;
}
</style>