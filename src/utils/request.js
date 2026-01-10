// src/utils/request.js
import axios from 'axios';

const service = axios.create({
    baseURL: 'http://localhost/api',
    timeout: 8000,
});

service.interceptors.response.use(
    res => res.data,
    err => {
        if (err.response.status === 401) {
            router.push('/login');
        }
        return Promise.reject(err)
    }
);

export default service;