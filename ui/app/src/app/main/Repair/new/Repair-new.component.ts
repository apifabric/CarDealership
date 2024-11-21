import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Repair-new',
  templateUrl: './Repair-new.component.html',
  styleUrls: ['./Repair-new.component.scss']
})
export class RepairNewComponent {
  @ViewChild("RepairForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}