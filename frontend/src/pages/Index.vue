<template>
  <q-page class="flex flex-center">
    <l-map
      :zoom="zoom"
      :center="center"
      :options="mapOptions"
      style="height: calc(100vh - 70px)"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
      @click="clickMap"
    >
      <l-tile-layer
        :url="url"
        :attribution="attribution"
      />
      <l-marker v-for="person in people" :key="person.id" :lat-lng="person.location">
        <l-icon
          :icon-size="[32, 32]"
          :icon-anchor="[16, 32]"
          icon-url="statics/icons/person.png" />
        <l-popup style="width:100px;" :options="{permanent: true, interactive: true}">
          <div @click="person.showInfo = !person.showInfo">
            {{person.name}}
            <p v-show="true">
              <img style="max-width:100px;" :src="person.photo || 'https://myrealdomain.com/images/icone-pessoa-png-6.png'" />

              <br />
              Contato (familiar):<br /> {{person.phone}}
              <br />
              <q-btn @click="removePerson(person.id)">Remover</q-btn>
            </p>
          </div>
        </l-popup>
      </l-marker>
      <l-marker v-for="animal in animals" :key="animal.id" :lat-lng="animal.location">
        <l-icon
          :icon-size="[32, 32]"
          :icon-anchor="[16, 32]"
          icon-url="statics/icons/animal.png" />
        <l-popup style="width:100px;" :options="{permanent: true, interactive: true}">
          <div @click="animal.showInfo = !animal.showInfo">
            {{animal.name}}
            <p v-show="true">
              <img style="max-width:100px;" :src="animal.photo || 'https://myrealdomain.com/images/icone-pessoa-png-6.png'" />
              <br />
              Contato (familiar):<br /> {{animal.phone}}
              <br />
              <q-btn @click="removePerson(person.id)">Remover</q-btn>
            </p>
          </div>
        </l-popup>
      </l-marker>
    </l-map>
    <q-modal v-model="showAddModal">
      <div style="width:300px; float:left;padding:4%;">
        <div class="row">
          <span>Cadastrar</span>
        </div>
        <div class="row">
          <span>Tipo</span>
            <q-field style="width: 100%;">
              <q-select

                v-model="currentSelection"
                :options="[
                  {
                    label: 'Pessoa',
                    icon: 'person',
                    value: 'pessoa'
                  },
                  {
                    label: 'Animal',
                    icon: 'pets',
                    value: 'animal'
                  },
                ]"
              />
            </q-field>
        </div>
        <div class="row">
          <q-field style="width: 100%;">
            <q-input v-model="form.name" float-label="Nome" />
          </q-field>
        </div>
        <div class="row">
          <q-field style="width: 100%;">
            <q-input v-model="form.phone" float-label="Telefone de contato (familiar)" />
          </q-field>
        </div>
        <div class="row fix-right" style="float:right;">
        <q-btn
          color="primary"
          @click="add"
          label="Cadastrar"
        />
        <q-btn
          color="red"
          @click="showAddModal = false"
          label="Cancelar"
        />
      </div>
      </div>
    </q-modal>

  </q-page>
</template>

<style>
#map {
  width: 100%;
  height: 100%;
}
</style>

<script>
import { L, LMap, LTileLayer, LMarker, LPopup, LTooltip, LIcon } from 'vue2-leaflet'

export default {
  name: 'PageIndex',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip,
    LIcon
  },
  data () {
    return {
      zoom: 14,
      addAnimalEvent: false,
      addPersonEvent: false,
      center: L.latLng(-20.135896, -44.123509),
      showAddModal: false,
      currentSelection: 'Pessoa',
      currentLocation: null,
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      iconSize: 64,
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      people: [
        {id: 1, name: 'João', photo: '', phone: '31 9999-9999', showInfo: true, location: L.latLng(-20.135896, -44.123509)},
        {id: 2, name: 'Marcelo', photo: '', phone: '31 9999-9999', showInfo: true, location: L.latLng(-20.145896, -44.123509)}
      ],
      animals: [],
      currentZoom: 14.5,
      currentCenter: L.latLng(47.413220, -1.219482),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5
      },
      form: {
        name: '',
        phone: '',
        photo: ''
      }
    }
  },
  computed: {
  },
  methods: {
    genID () {
      var S4 = function () {
        return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1)
      }
      return (S4() + S4() + '-' + S4() + '-' + S4() + '-' + S4() + '-' + S4() + S4() + S4())
    },
    add () {
      if (this.currentSelection === 'pessoa') {
        this.people.push({id: this.genID(), name: this.form.name, phone: this.form.phone, location: this.currentLocation})
      } else {
        this.animals.push({id: this.genID(), name: this.form.name, phone: this.form.phone, location: this.currentLocation})
      }
      this.showAddModal = false
    },
    clickMap (event) {
      console.log(event)
      this.currentLocation = event.latlng
      this.showAddModal = true
    },
    addPerson () {
      this.currentSelection = 'Pessoa'
    },
    addAnimal () {
      this.currentSelection = 'Animal'
    },
    removePerson (id) {
      this.people = this.people.filter(function (el) { return el.id !== id })
    },
    removeAnimal () {
      // this.animals = this.animals.filter(function (el) { return el.id !== id })
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
    console.log(LMap)
  }
}
</script>
