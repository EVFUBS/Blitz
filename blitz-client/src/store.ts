import { writable } from "svelte/store";

export const group = writable({
    group_id: undefined,
    group_name: undefined,
    group_description: undefined,
    category_id: undefined,
    author: undefined
});

export const csrf = writable(undefined);

export const loggedIn = writable(false);

export const theme = writable(false)
export const themeColor = writable('#1B2430')
export const themeColor2 = writable('white')
export const themeColorAlt = writable('#ECDBBA')
