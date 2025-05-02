<template>
  <div class="register-event-page">
    <div class="register-event-form">
      <h1 class="page-title">Register Event</h1>
      <form @submit.prevent="handleRegister" class="form">
        <div class="form-group">
          <label for="eventName">Event Name:</label>
          <input id="eventName" v-model="eventName" type="text" required />
        </div>
        <div class="form-group">
          <label for="address">Event Address:</label>
          <input id="address" v-model="address" type="text" required />
        </div>
        <div class="form-group">
          <label for="eventTime">Event Time:</label>
          <input id="eventTime" v-model="eventTime" type="datetime-local" required />
        </div>
        <button type="submit" class="btn">Register Event</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const eventName = ref('')
const address = ref('')
const eventTime = ref('')

const handleRegister = () => {
  alert(`Registering event: ${eventName.value} at ${address.value} on ${eventTime.value}`)
  // TODO: Implement actual event registration logic
}
</script>

<style scoped>
/* Laz: Added a new div and changes the OG register-event-page to register-event-form, that way you can edit the background as well. */
.register-event-page {
  min-height: 100vh;
  background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
  /* Laz: Do not add flex unless you decide to further detail the widths */
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.register-event-form {
  max-width: 500px;
  margin: 2rem auto;
  border: 2px solid var(--pnw-gold);
  padding: 2rem;
  background: var(--pnw-white);
  border-radius: 0.75rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.page-title {
  font-size: 2rem;
  color: var(--pnw-gold);
  text-align: center;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--pnw-black);
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
}

.btn {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--pnw-gold);
  color: var(--pnw-black);
  font-weight: 700;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #bfa32f;
}
</style>
