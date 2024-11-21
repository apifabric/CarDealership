import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SALESPERSON_MODULE_DECLARATIONS, SalespersonRoutingModule} from  './Salesperson-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SalespersonRoutingModule
  ],
  declarations: SALESPERSON_MODULE_DECLARATIONS,
  exports: SALESPERSON_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SalespersonModule { }