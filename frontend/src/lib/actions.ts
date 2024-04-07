'use server'
import { unstable_noStore as noStore } from "next/cache";
const ENDPOINT = process.env.API_END_POINT 
if (!ENDPOINT) {
    throw new Error('API_END_POINT is not defined')
}
console.log("====================================");
console.log(ENDPOINT);
console.log("====================================");
export const testFetch = async () => {
    noStore();
    const res = await fetch(ENDPOINT, {
        headers: {
        "Content-Type": "application/json",
        },
    });
    const data = await res.text();
    console.log(data);
    return data;
}