import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ServiceHomeComponent } from './home/Service-home.component';
import { ServiceNewComponent } from './new/Service-new.component';
import { ServiceDetailComponent } from './detail/Service-detail.component';

const routes: Routes = [
  {path: '', component: ServiceHomeComponent},
  { path: 'new', component: ServiceNewComponent },
  { path: ':id', component: ServiceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Service-detail-permissions'
      }
    }
  },{
    path: ':service_id/Repair', loadChildren: () => import('../Repair/Repair.module').then(m => m.RepairModule),
    data: {
        oPermission: {
            permissionId: 'Repair-detail-permissions'
        }
    }
}
];

export const SERVICE_MODULE_DECLARATIONS = [
    ServiceHomeComponent,
    ServiceNewComponent,
    ServiceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ServiceRoutingModule { }