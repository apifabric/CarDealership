import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ACCESSORY_MODULE_DECLARATIONS, AccessoryRoutingModule} from  './Accessory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AccessoryRoutingModule
  ],
  declarations: ACCESSORY_MODULE_DECLARATIONS,
  exports: ACCESSORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AccessoryModule { }