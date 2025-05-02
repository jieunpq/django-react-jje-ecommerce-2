import { createRoot } from 'react-dom/client'
import { RouterProvider } from 'react-router-dom'
import { router } from './router/Router.jsx'
import { AuthProvider } from '@/contexts/AuthContext' // ⬅️ 이 줄 추가

//dev_1_fruit
createRoot(document.getElementById('root')).render(
  <AuthProvider>
    <RouterProvider router={router} />
  </AuthProvider>
)
