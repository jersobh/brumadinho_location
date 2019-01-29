<template>
  <q-page class="flex flex-center">
    <l-map
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: calc(100vh - 70px)"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
      @click="clickMap()"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker v-for="person in people" :key="person.id" :lat-lng="person.location">
        <l-popup style="width:100px;" :options="{permanent: true, interactive: true}">
          <div @click="person.showInfo = !person.showInfo">
            {{person.name}}
            <p v-show="true">
              <img style="max-width:100px;" :src="person.photo || 'https://myrealdomain.com/images/icone-pessoa-png-6.png'" />
              <br />
              Funcionário: {{person.worker}}
              <br />
              Contato (familiar):<br /> {{person.phone}}
              <br />
              <q-btn @click="removePerson(person.id)">Remover</q-btn>
            </p>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
    <q-fab
  color="red-7"
  icon="add"
  direction="up"
  class="fixed"
  style="right: 30px; bottom: 30px"
>
<q-fab-action
  color="red-5"
  @click="addAnimal()"
  icon="pets"
/>
  <q-fab-action
    color="red-5"
    @click="addPerson()"
    icon="person"
  />
</q-fab>
  </q-page>
</template>

<style>
#map {
  width: 100%;
  height: 100%;
}
</style>

<script>
import { L, LMap, LTileLayer, LMarker, LPopup, LTooltip } from 'vue2-leaflet'

export default {
  name: 'PageIndex',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip
  },
  data () {
    return {
      zoom: 14,
      center: L.latLng(-20.135896, -44.123509),
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      people: [
        {id: 1, name: 'João', photo: '', worker: 'Sim', phone: '31 9999-9999', showInfo: true, location: L.latLng(-20.135896, -44.123509)},
        {id: 2, name: 'Marcelo', photo: '', worker: 'Não', phone: '31 9999-9999', showInfo: true, location: L.latLng(-20.145896, -44.123509)}
      ],
      animal: [],
      currentZoom: 14.5,
      currentCenter: L.latLng(47.413220, -1.219482),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      }
    }
  },
  methods: {
    clickMap (event) {
      console.log(event)
    },
    addPerson () {

    },
    addAnimal () {
    },
    removePerson (id) {
      this.people = this.people.filter(function (el) { return el.id !== id })
    },
    removeAnimal () {

    },
    zoomUpdate (zoom) {
      this.currentZoom = zoom
    },
    centerUpdate (center) {
      this.currentCenter = center
    },
    showLongText () {
      this.showParagraph = !this.showParagraph
    },
    innerClick () {
      alert('Click!')
    }
  },
  mounted () {
  }
}
</script>
