import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';

const dev = process.argv.includes('dev');

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter(),
    prerender:{
      entries: ['/leagues/*'],
    },
    paths: {
        base: dev ? '/base' : process.env.BASE_PATH,
    }
},
  preprocess: vitePreprocess()
};

export default config;