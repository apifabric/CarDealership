import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Warranty-new',
  templateUrl: './Warranty-new.component.html',
  styleUrls: ['./Warranty-new.component.scss']
})
export class WarrantyNewComponent {
  @ViewChild("WarrantyForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}