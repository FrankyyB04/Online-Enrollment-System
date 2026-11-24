document.addEventListener('DOMContentLoaded', () => {
    // Profile category tabs on dashboard
    const tabButtons = document.querySelectorAll('.tab-btn');
    const infoCards = document.querySelectorAll('.info-card');

    tabButtons.forEach((btn) => {
        btn.addEventListener('click', () => {
            tabButtons.forEach((b) => b.classList.remove('active'));
            btn.classList.add('active');

            const target = btn.getAttribute('data-target');
            infoCards.forEach((card) => {
                if (target === 'all' || card.getAttribute('data-category') === target) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });

    // Dismiss alert banners
    document.querySelectorAll('.alert-close').forEach((closeBtn) => {
        closeBtn.addEventListener('click', () => {
            const banner = closeBtn.closest('.alert-banner');
            if (banner) banner.remove();
        });
    });

    // Quick sample fill button on registration page for easy testing
    const fillDemoBtn = document.getElementById('fillDemoBtn');
    if (fillDemoBtn) {
        fillDemoBtn.addEventListener('click', () => {
            const rand = Math.floor(100 + Math.random() * 899);
            const demoValues = {
                id_program: 'BS Information Technology',
                id_class_section: 'BSIT 3-A',
                id_year_level: '3rd Year',
                id_academic_term: '1st Semester, AY 2026-2027',
                id_enrollment_status: 'Enrolled',
                id_first_name: 'Andrea',
                id_middle_name: 'Mercado',
                id_last_name: `Castillo-${rand}`,
                id_date_of_birth: '2005-05-14',
                id_gender: 'Female',
                id_nationality: 'Filipino',
                id_email: `andrea.castillo${rand}@student.edu`,
                id_phone_number: '+63 917 554 8812',
                id_home_address: '56 Evangelista Street, Brgy. 4, Lucena City, Quezon',
                id_emergency_contact_name: 'Carmela Mercado Castillo',
                id_emergency_contact_relation: 'Mother',
                id_emergency_contact_phone: '+63 918 441 9920',
                id_previous_school: 'Quezon National High School',
                id_school_type: 'Public High School',
                id_graduation_year: '2024',
                id_previous_gpa: '1.40',
                id_honors_awards: 'With Honors',
                id_guardian_name: 'Carmela Mercado Castillo',
                id_guardian_occupation: 'Public School Teacher',
                id_guardian_contact: '+63 918 441 9920',
                id_scholarship_status: 'Academic Scholar (50%)',
                id_admin_notes: 'Registered via front-end student enrollment portal.',
            };

            Object.entries(demoValues).forEach(([id, val]) => {
                const el = document.getElementById(id);
                if (el) el.value = val;
            });
        });
    }
});
