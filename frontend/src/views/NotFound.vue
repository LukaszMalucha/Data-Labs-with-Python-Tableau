<template>
<div id="page-index">
  <RowHeaderComponent/>
  <div class="row row-banner">
    <div class="col-md-12 text-center col-banner plain-element">
      <h4>404 - Page Not Found</h4>
    </div>
  </div>
</div>
</template>


<script>
import RowHeaderComponent from "@/components/RowHeader.vue";


export default {
  name: "NotFound",
  components: {
    RowHeaderComponent,
  },

}
</script>