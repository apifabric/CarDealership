import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WarrantyHomeComponent } from './home/Warranty-home.component';
import { WarrantyNewComponent } from './new/Warranty-new.component';
import { WarrantyDetailComponent } from './detail/Warranty-detail.component';

const routes: Routes = [
  {path: '', component: WarrantyHomeComponent},
  { path: 'new', component: WarrantyNewComponent },
  { path: ':id', component: WarrantyDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Warranty-detail-permissions'
      }
    }
  }
];

export const WARRANTY_MODULE_DECLARATIONS = [
    WarrantyHomeComponent,
    WarrantyNewComponent,
    WarrantyDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class WarrantyRoutingModule { }