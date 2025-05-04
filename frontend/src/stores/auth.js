import { ref } from 'vue'

const isLoggedIn = ref(false)
const user = ref(null)

export function useAuth() {
  const login = (userData) => {
    user.value = userData
    isLoggedIn.value = true
    localStorage.setItem('user', JSON.stringify(userData))
  }

  const logout = () => {
    user.value = null
    isLoggedIn.value = false
    localStorage.removeItem('user')
  }

  const checkLoginStatus = () => {
    const storedUser = localStorage.getItem('user')
    if (storedUser) {
      user.value = JSON.parse(storedUser)
      isLoggedIn.value = true
    } else {
      user.value = null
      isLoggedIn.value = false
    }
  }

  return {
    isLoggedIn,
    user,
    login,
    logout,
    checkLoginStatus
  }
} 