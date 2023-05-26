<script>
  export let isOpen = false;
</script>

<div class="navbar bg-base-100">
    <div class="flex-1">
      <a on:click={()=> isOpen = !isOpen}  href="/" class="btn btn-ghost normal-case text-xl">LaStats</a>
    </div>
    <div class="flex-none">
      <ul class="menu menu-horizontal {isOpen ? " drawer-toggle" : ''}  px-1">
        <li><a  href="#">Ligi</a></li>
        <li>
          <a href="#" tabindex="0">
            Statystyki
            <svg class="fill-current" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/></svg>
          </a>
          <ul class="p-2 bg-base-100">
            <li><a href="#">Zawodnicy</a></li>
            <li><a href="#">Druzyny</a></li>
          </ul>
        </li>
        <li>
          <a href="#" tabindex="0">
            Dodaj
            <svg class="fill-current" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/></svg>
          </a>
          <ul class="p-2 bg-base-100">
            <li><a href="#">Ligę</a></li>
            <li><a href="#">Zawodnika</a></li>
            <li><a href="#">Drużynę</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>