import { toast } from '@zerodevx/svelte-toast';

export const successToast = (message: string) => {
	toast.push(message, {
		theme: {
			'--toastBackground': '#059669',
			'--toastColor': '#fff'
		}
	});
};

export const errorToast = (message: string) => {
	toast.push(message, {
		theme: {
			'--toastBackground': '#cf2929',
			'--toastColor': '#fff'
		}
	});
};
