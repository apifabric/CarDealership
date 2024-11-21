import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RepairHomeComponent } from './home/Repair-home.component';
import { RepairNewComponent } from './new/Repair-new.component';
import { RepairDetailComponent } from './detail/Repair-detail.component';

const routes: Routes = [
  {path: '', component: RepairHomeComponent},
  { path: 'new', component: RepairNewComponent },
  { path: ':id', component: RepairDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Repair-detail-permissions'
      }
    }
  }
];

export const REPAIR_MODULE_DECLARATIONS = [
    RepairHomeComponent,
    RepairNewComponent,
    RepairDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RepairRoutingModule { }