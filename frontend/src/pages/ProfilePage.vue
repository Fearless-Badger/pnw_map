<template>
  <div class="profile-page">
    <div class="profile-container">
      <h1 class="page-title">My Profile</h1>
      <div class="profile-info" v-if="user">
        <div class="info-item">
          <span class="label">Name:</span>
          <span class="value">{{ user.fname }} {{ user.lname }}</span>
        </div>
        <div class="info-item">
          <span class="label">Email:</span>
          <span class="value">{{ user.email }}</span>
        </div>
        <div class="info-item">
          <span class="label">Student ID:</span>
          <span class="value">{{ user.student_id }}</span>
        </div>
      </div>
      <button @click="handleLogout" class="logout-button">Logout</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const auth = inject('auth')
const user = ref(null)

onMounted(() => {
  if (auth.user.value) {
    user.value = auth.user.value
  } else {
    router.push('/login')
  }
})

const handleLogout = async () => {
  auth.logout()
  await router.push('/login')
}
</script>

<style scoped>
.profile-page {
  min-height: 100vh;
  background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
  padding: 2rem;
}

.profile-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: var(--pnw-white);
  border: 2px solid var(--pnw-gold);
  border-radius: 0.75rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}

.page-title {
  font-size: 2rem;
  color: var(--pnw-gold);
  text-align: center;
  margin-bottom: 2rem;
}

.profile-info {
  margin-bottom: 2rem;
}

.info-item {
  display: flex;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid #eee;
}

.info-item:last-child {
  border-bottom: none;
}

.label {
  font-weight: 600;
  color: var(--pnw-black);
}

.value {
  color: #666;
}

.logout-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #dc3545;
  color: white;
  font-weight: 700;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.logout-button:hover {
  background-color: #c82333;
}
</style> 