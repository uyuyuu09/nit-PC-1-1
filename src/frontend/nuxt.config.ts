// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
import { resolve } from "path";
import { readFileSync } from "fs";
export default defineNuxtConfig({
    compatibilityDate: "2025-05-15",
    devtools: { enabled: true },
    vite: {
        plugins: [tailwindcss()],
    },
    css: ["~/assets/css/main.css"],
    devServer: {
        https: {
            key: readFileSync(
                resolve(__dirname, "localhost+3-key.pem"),
                "utf-8"
            ),
            cert: readFileSync(resolve(__dirname, "localhost+3.pem"), "utf-8"),
        },
        host: "0.0.0.0",
    },
    modules: ["@pinia/nuxt", "pinia-plugin-persistedstate/nuxt"],
    runtimeConfig: {
        public: {
            BASE_API: process.env.BASE_API || "",
            GET_ALL_QUESTION: process.env.GET_ALL_QUESTION || "",
            CREATE_QUESTION: process.env.CREATE_QUESTION || "",
            DELETE_QUESTION: process.env.DELETE_QUESTION || "",
        },
    },
});
