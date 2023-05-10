<template>
  <div class="card cert-card">
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="title is-4">{{ certification.certification_name }}</p>
          <p class="subtitle is-6">Issued {{ certification.date_achieved }}</p>
        </div>
      </div>
      <div class="content">
        {{ certification.description }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CertCard",
  props: {
    certification: {
      type: Object,
    },
  },
};
</script>

<style>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
