import { createContext, useContext, useState } from "react";
import { getCurrentUser, loginUser } from "@/api/AuthApi";

// Context 생성
const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

// Provider 컴포넌트
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState(localStorage.getItem("access"));

  const login = async (username, password) => {
    try {
      const response = await loginUser(username, password);
      const { access, refresh } = response.data;

      // 저장 영역은 크게 4 가지 정도 있음
      // 1.local storage 2.session storage 3.cookie 
      localStorage.setItem("access", access);
      localStorage.setItem("refresh", refresh);
      setAccessToken(access);
      // 이후 getUser() 등을 통해 사용자 정보 fetch 가능

    } catch (error) {
      console.error("로그인 실패:", error);
      throw error;
    }
  };

  const getUser = async () => {
    try{
      const response = await getCurrentUser()
      setUser(response.data)
      console.log(response.data)

    }catch(error){
      console.error("사용자 정보 받아오기 실패", error)
      logout()
    }
  }

  // 로그아웃 시 로컬에 저장된 access 토큰과 refresh 토큰을 삭제만 하면 됨
  const logout = () => {
    setUser(null);
    setAccessToken(null);
    localStorage.removeItem("access");
    localStorage.reomveItem("refresh")
  }


  const value = {
    logout,
    login,
    accessToken,
    user,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
