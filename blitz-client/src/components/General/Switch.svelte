<script lang="ts">
export let val: boolean = false;
</script>

<input bind:checked={val} on:click type="checkbox" id="switch" />
<label for="switch">Toggle</label>

<style>
    input[type=checkbox]{
	height: 0;
	width: 0;
	visibility: hidden;
}

label {
	cursor: pointer;
	text-indent: -9999px;
	width: 60px;
	height: 25px;
	background: var(--theme-color-2);
	display: block;
	border-radius: 100px;
	position: relative;
}

label:after {
	content: '';
	position: absolute;
	top: 5px;
	left: 5px;
	width: 16px;
	height: 16px;
	background: var(--theme-color);
	border-radius: 90px;
	transition: 0.3s;
}

input:checked + label {
	background: var(--theme-color-alt);
}

input:checked + label:after {
	left: calc(100% - 5px);
	transform: translateX(-100%);
}

label:active:after {
	width: 30px;
}
</style>