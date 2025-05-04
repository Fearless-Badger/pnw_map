<template>
  <div class="events-page">
    <div class="events-container">
      <h1 class="events-title">Upcoming Campus Events</h1>

      <div v-if="loading" class="loading-message">
        Loading events...
      </div>
      <div v-else-if="error" class="error-message">
        {{ error }}
      </div>
      <div v-else>
        <div class="events-list">
          <div v-for="event in events" :key="event.event_id" class="event-card" @click="selectedEvent = event" style="cursor: pointer">
            <h2 class="event-name">{{ event.event_name }}</h2>
            <p class="event-info">📅 {{ formatDate(event.date) }} — 📍 {{ formatLocation(event) }}</p>
            <p class="event-description">{{ event.abstract }}</p>
            <p class="event-cost" v-if="event.cost">Cost: ${{ event.cost }}</p>
          </div>
        </div>

        <div class="map-placeholder">
          <iframe
            width="1000"
            height="300"
            style="border: 0"
            loading="lazy"
            allowfullscreen
            referrerpolicy="no-referrer-when-downgrade"
            :src="iframeSrc"
          >
          </iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const events = ref([])
const loading = ref(true)
const error = ref(null)
const selectedEvent = ref(null)

const fetchEvents = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await fetch('http://localhost:8000/api/events/')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    events.value = data
  } catch (err) {
    error.value = `Error loading events: ${err.message}`
    console.error('Error fetching events:', err)
  } finally {
    loading.value = false
  }
}

const formatDate = (dateString) => {
  if (!dateString) return 'Date not set'
  try {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  } catch (err) {
    console.error('Error formatting date:', err)
    return 'Invalid date'
  }
}

const formatLocation = (event) => {
  if (!event) return 'Location not set'
  return `${event.street_address}, ${event.city}, ${event.state} ${event.zip_code}`
}

const iframeSrc = computed(() => {
  const base = 'https://www.google.com/maps/embed/v1/place'
  const apiKey = import.meta.env.VITE_GOOGLE_API_KEY
  const query = selectedEvent.value 
    ? `${selectedEvent.value.street_address}, ${selectedEvent.value.city}, ${selectedEvent.value.state} ${selectedEvent.value.zip_code}`
    : 'Purdue Northwest University'
  return `${base}?key=${apiKey}&q=${encodeURIComponent(query)}`
})

onMounted(() => {
  fetchEvents()
})
</script>

<style scoped>
.events-page {
  min-height: 100vh;
  padding: 2rem;
  background: linear-gradient(to bottom, var(--pnw-white), #f3f4f6);
}

.events-container {
  max-width: 1000px;
  margin: 0 auto;
}

.events-title {
  font-size: 2.5rem;
  font-weight: bold;
  color: var(--pnw-gold);
  text-align: center;
  margin-bottom: 2rem;
}

.loading-message,
.error-message {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
  color: var(--pnw-black);
}

.error-message {
  color: #dc3545;
}

.events-list {
  display: grid;
  gap: 2rem;
}

.event-card {
  background-color: var(--pnw-white);
  border: 1px solid #ccc;
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: transform 0.3s, box-shadow 0.3s;
}

.event-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.event-name {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--pnw-black);
  margin-bottom: 0.5rem;
}

.event-info {
  font-size: 0.9rem;
  color: var(--pnw-gray);
  margin-bottom: 1rem;
}

.event-description {
  color: #444444;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.event-cost {
  color: var(--pnw-gold);
  font-weight: 600;
  font-size: 1rem;
}

.map-placeholder {
  background-color: #e5e7eb;
  border-radius: 0.75rem;
  height: 300px;
  margin-top: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #555555;
  font-size: 1.2rem;
  font-style: italic;
}
</style>
