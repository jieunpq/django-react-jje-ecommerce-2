import http from './HttpCommon'; // axios 인스턴스

// # 경로    설명
// # POST /auth/jwt/create/    로그인 (토큰 발급)
// # POST /auth/jwt/refresh/    액세스 토큰 갱신
// # POST /auth/jwt/verify/    토큰 유효성 확인
// # POST /auth/users/    회원가입
// # GET /auth/users/me/    현재 로그인된 사용자 조회
// http://127.0.0.1:8000/api/

// 로그인 요청: access, refresh 토큰 받기
export const loginUser = (username, password) => {
    return http.post("/api/auth/jwt/create/", {
        username,
        password
    });
}

// 현재 로그인 된 사용자 조회
export const getCurrentUser = () => {
    return http.post("/api/auth/users/me");
}


