import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import time
import const
from prediction import predict

st.set_page_config(layout="wide")
st.title("Skin Disease Classification")


def get_class(label):
    return list(filter(lambda x: x['label'] == label, const.classes.values()))[0]["name"]



col1, col2 = st.columns(2)
disease = ""

with col1:
    uploaded_file = st.file_uploader("Upload a skin image sample", type=["png","jpg","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded skin image', use_column_width=True)
        label = predict(image)
        disease = get_class(label)
with col2:
    if disease != "":
        st.markdown(f'<p style="font-size:36px;border-radius:2%;">Prediction: <span style="font-weight:bold;">{disease}</span></p>', unsafe_allow_html=True)
        st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
        st.header("MANAGEMENT AND TREATMENT")
    if disease == "Benign keratosis-like lesions":
        st.subheader("How is seborrheic keratosis treated?")
        st.write("You should always have new skin growths clinically diagnosed to make sure they aren’t cancerous. Different kinds of skin growths can be hard to tell apart from each other. If your healthcare provider is in any doubt about your growth, they might want to remove it for biopsy.")

        st.write("If it is clearly a seborrheic keratosis, it won’t require any treatment. But you might want to have it removed if it becomes itchy or irritated or you don’t like the look of it. Your healthcare provider can remove it for you in the office using one of several common methods.")

        st.subheader("How is seborrheic keratosis removed?")
        st.write("Medical offices offer several options for removing your seborrheic keratosis:")

        st.markdown("1. Cryotherapy. Your healthcare provider will numb the skin and then use liquid nitrogen to freeze the growth. This will cause it to fall off within a few days or weeks. Cryotherapy is a common choice when the diagnosis is clear and there is no need to preserve a sample of the growth for biopsy. One possible side effect is that the skin where the growth was will lose some of its pigment and look lighter.")
        st.markdown("2. Electrodessication/Curettage. Your healthcare provider will numb the skin and then use a targeted electrocurrent to burn the seborrheic keratosis. They use a surgical instrument called a curette to scrape away the remains of the growth. Electrodessication and curettage are also sometimes used individually. The risk of scarring is generally low with both methods, but there is some wound care involved afterward.")
        st.markdown("3. Shave Excision. This is the preferred method when your healthcare provider wants to preserve a sample of the growth to analyze in the lab. After numbing the skin, your healthcare provider will carefully shave off the growth and smooth the skin underneath with a surgical curette. Then they’ll send the shaved growth to the lab for analysis.")
        st.markdown("4. Laser Therapy. Lasers offer an alternative to surgery by burning the growth, sterilizing the wound and sealing the tissue all at once. Laser therapy is quick, but the wound will be sore for a while afterward. Lasers are associated with good cosmetic results.")
        st.markdown("5. Prescription Hydrogen Peroxide. The FDA has recently approved a topical solution of 40% hydrogen peroxide to treat seborrheic keratosis. (Over-the-counter hydrogen peroxide is a 1% solution.) The solution comes in an applicator pen, which your healthcare provider will apply to your seborrheic keratosis several times in one visit. You may need more than one visit to see results. Mild skin reactions are a common side effect.")

        st.subheader("Is there an over-the-counter treatment for seborrheic keratosis?")
        st.write("Some over-the-counter topical treatments have shown promise for reducing seborrheic keratoses. Research is limited on these solutions. They take time and persistence to work and are not 100% effective. But they also have fewer side effects and little-to-no recovery time. They might be a practical option to try if you want to treat many growths at once. Options include:")

        st.markdown("- Tazarotene cream 0.1%.")
        st.markdown("- Alpha Hydroxy Acid (AHA) products, including glycolic acid and salicylic acid peels.")
        st.markdown("- Vitamin D3 cream.")
    elif disease == "Melanocytic nevi":
        st.write("Most melanocytic naevi are harmless and can be safely left alone. They may be removed in the following circumstances:")

        st.markdown("- To exclude cancer")
        st.markdown("- If a naevus is a nuisance: perhaps irritated by clothing, comb or razor")
        st.markdown("- Cosmetic reasons: the mole is unsightly.")
        
        st.write("Surgical techniques include:")

        st.markdown("- Excision biopsy of a flat or suspicious melanocytic naevus")
        st.markdown("- Shave biopsy of a protruding melanocytic naevus")
        st.markdown("- Electrosurgical destruction")
        st.markdown("- Laser to lessen pigment or remove coarse hair.")
    elif disease == "Melanoma":
        st.write("The best treatment for your melanoma depends on the size and stage of cancer, your overall health, and your personal preferences.")

        st.subheader("Treatment for small melanomas")
        st.write("Treatment for early-stage melanomas usually includes surgery to remove the melanoma. A very thin melanoma may be removed entirely during the biopsy and require no further treatment. Otherwise, your surgeon will remove the cancer as well as a border of normal skin and a layer of tissue beneath the skin. For people with early-stage melanomas, this may be the only treatment needed.")

        st.subheader("Treating melanomas that have spread beyond the skin")
        st.write("If melanoma has spread beyond the skin, treatment options may include:")

        st.markdown("- **Surgery to remove affected lymph nodes.** If melanoma has spread to nearby lymph nodes, your surgeon may remove the affected nodes. Additional treatments before or after surgery also may be recommended.")
        st.markdown("- **Immunotherapy.** Immunotherapy is a drug treatment that helps your immune system to fight cancer. Your body's disease-fighting immune system might not attack cancer because the cancer cells produce proteins that help them hide from the immune system cells. Immunotherapy works by interfering with that process. Immunotherapy is often recommended after surgery for melanoma that has spread to the lymph nodes or to other areas of the body. When melanoma can't be removed completely with surgery, immunotherapy treatments might be injected directly into the melanoma.")

        st.markdown("- **Targeted therapy.** Targeted drug treatments focus on specific weaknesses present within cancer cells. By targeting these weaknesses, targeted drug treatments can cause cancer cells to die. Cells from your melanoma may be tested to see if targeted therapy is likely to be effective against your cancer. For melanoma, targeted therapy might be recommended if the cancer has spread to your lymph nodes or to other areas of your body.")

        st.markdown("- **Radiation therapy.** This treatment uses high-powered energy beams, such as X-rays and protons, to kill cancer cells. Radiation therapy may be directed to the lymph nodes if the melanoma has spread there. Radiation therapy can also be used to treat melanomas that can't be removed completely with surgery. For melanoma that spreads to other areas of the body, radiation therapy can help relieve symptoms.")

        st.markdown("- **Chemotherapy.** Chemotherapy uses drugs to kill cancer cells. Chemotherapy can be given intravenously, in pill form or both so that it travels throughout your body. Chemotherapy can also be given in a vein in your arm or leg in a procedure called isolated limb perfusion. During this procedure, blood in your arm or leg isn't allowed to travel to other areas of your body for a short time so that the chemotherapy drugs travel directly to the area around the melanoma and don't affect other parts of your body.")
    elif disease == "Basal cell carcinoma":
        st.write("The goal of treatment for basal cell carcinoma is to remove the cancer completely. Which treatment is best for you depends on the type, location and size of your cancer, as well as your preferences and ability to do follow-up visits. Treatment selection can also depend on whether this is a first-time or a recurring basal cell carcinoma.")

        st.subheader("Surgery")
        st.write("Basal cell carcinoma is most often treated with surgery to remove all of the cancer and some of the healthy tissue around it.")

        st.write("Options might include:")

        st.markdown("- **Surgical excision.** In this procedure, your doctor cuts out the cancerous lesion and a surrounding margin of healthy skin. The margin is examined under a microscope to be sure there are no cancer cells. Excision might be recommended for basal cell carcinomas that are less likely to recur, such as those that form on the chest, back, hands and feet.")

        st.markdown("- **Mohs surgery.** During Mohs surgery, your doctor removes the cancer layer by layer, examining each layer under the microscope until no abnormal cells remain. This allows the surgeon to be certain the entire growth is removed and avoid taking an excessive amount of surrounding healthy skin. Mohs surgery might be recommended if your basal cell carcinoma has a higher risk of recurring, such as if it's larger, extends deeper in the skin or is located on your face.")

        st.subheader("Other treatments")
        st.write("Sometimes other treatments might be recommended in certain situations, such as if you're unable to undergo surgery or if you don't want to have surgery.")

        st.write("Other treatments include:")

        st.markdown("- **Curettage and electrodessication (C and E).** C and E treatment involves removing the surface of the skin cancer with a scraping instrument (curet) and then searing the base of the cancer with an electric needle. C and E might be an option for treating small basal cell carcinomas that are less likely to recur, such as those that form on the back, chest, hands and feet.")

        st.markdown("- **Radiation therapy.** Radiation therapy uses high-energy beams, such as X-rays and protons, to kill cancer cells. Radiation therapy is sometimes used after surgery when there is an increased risk that the cancer will return. It might also be used when surgery isn't an option.")

        st.markdown("- **Freezing.** This treatment involves freezing cancer cells with liquid nitrogen (cryosurgery). It may be an option for treating superficial skin lesions. Freezing might be done after using a scraping instrument (curet) to remove the surface of the skin cancer. Cryosurgery might be considered for treating small and thin basal cell carcinomas when surgery isn't an option.")

        st.markdown("- **Topical treatments.** Prescription creams or ointments might be considered for treating small and thin basal cell carcinomas when surgery isn't an option.")

        st.markdown("- **Photodynamic therapy.** Photodynamic therapy combines photosensitizing drugs and light to treat superficial skin cancers. During photodynamic therapy, a liquid drug that makes the cancer cells sensitive to light is applied to the skin. Later, a light that destroys the skin cancer cells is shined on the area. Photodynamic therapy might be considered when surgery isn't an option.")

        st.subheader("Treatment for cancer that spreads")
        st.write("Very rarely, basal cell carcinoma may spread (metastasize) to nearby lymph nodes and other areas of the body. Additional treatment options in this situation include:")

        st.markdown("- **Targeted drug therapy.** Targeted drug treatments focus on specific weaknesses present within cancer cells. By blocking these weaknesses, targeted drug treatments can cause cancer cells to die. Targeted therapy drugs for basal cell carcinoma block molecular signals that enable the cancers to continue growing. They might be considered after other treatments or when other treatments aren't possible.")

        st.markdown("- **Chemotherapy.** Chemotherapy uses powerful drugs to kill cancer cells. It might be an option when other treatments haven't helped.")
    elif disease == "Actinic keratoses":
        st.write("An actinic keratosis sometimes disappears on its own but might return after more sun exposure. It's hard to tell which actinic keratoses will develop into skin cancer, so they're usually removed as a precaution.")

        st.subheader("Medications")
        st.write("If you have several actinic keratoses, your doctor might prescribe a medicated cream or gel to remove them, such as fluorouracil (Carac, Fluoroplex, others), imiquimod (Aldara, Zyclara), ingenol mebutate or diclofenac (Solaraze). These products might cause redness, scaling or a burning sensation for a few weeks.")

        st.subheader("Surgical and other procedures")
        st.write("Many methods are used to remove actinic keratosis, including:")

        st.markdown("- **Freezing (cryotherapy).** Actinic keratoses can be removed by freezing them with liquid nitrogen. Your doctor applies the substance to the affected skin, which causes blistering or peeling. As your skin heals, the damaged cells slough off, allowing new skin to appear. Cryotherapy is the most common treatment. It takes only a few minutes and can be done in your doctor's office. Side effects may include blisters, scarring, changes to skin texture, infection and changes in skin color of the affected area.")
        st.markdown("- **Scraping (curettage).** In this procedure, your doctor uses a device called a curet to scrape off damaged cells. Scraping may be followed by electrosurgery, in which the doctor uses a pencil-shaped instrument to cut and destroy the affected tissue with an electric current. This procedure requires local anesthesia. Side effects may include infection, scarring and changes in skin color of the affected area.")
        st.markdown("- **Laser therapy.** This technique is increasingly used to treat actinic keratosis. Your doctor uses an ablative laser device to destroy the patch, allowing new skin to appear. Side effects may include scarring and discoloration of the affected skin.")
        st.markdown("- **Photodynamic therapy.** Your doctor might apply a light-sensitive chemical solution to the affected skin and then expose it to a special light that will destroy the actinic keratosis. Side effects may include redness, swelling and a burning sensation during therapy.")
    elif disease == "Vascular lesions":
        st.markdown("**Medication**: Patients may be placed on medications such as oral corticosteroids like prednisone or an oral blood pressure medication called propranolol, in order to help slow the rapid growth phase and promote involution. These medications can be effective, but have some side effects that make careful patient selection and monitoring important. Bulky hemangiomas may sometimes benefit from an injection of a corticosteroid into the lesion, which is usually done under a brief anesthetic. Other medications (such as interferon given by serial injection) can have more serious potential side effects, and are reserved for patients with extensive lesions that do not respond to other therapies.")

        st.markdown("**Surgery**: The surgical treatment of hemangiomas must carefully balance the need for early treatment with the scarring that will be created by the procedure. Because most lesions undergo at least a fair amount of involution on their own, it is important to delay most surgery until this occurs to allow tissue to stabilize before reconstruction. This will maximize healing and minimize the length of scars. An exception to waiting may occur if surgery provides the quickest option to relieve obstruction or allows better staging of reconstruction the lesion(s). These situations are best determined by an experienced pediatric plastic surgeon.")

        st.markdown("**Laser Therapy**: Finally, laser therapy can be used to treat ulcerated lesions, as well as any residual blood vessels or discoloration that may remain after involution. Extensive airway lesions may also require CO2 laser therapy for management, which is carried out by an otolaryngologist (ENT surgeon) under anesthesia.")
    elif disease == "Dermatofibroma":
        st.write("Because they’re noncancerous, dermatofibromas don’t always require treatment.")

        st.write("If a dermatofibroma is large or causes discomfort, your healthcare provider may remove it. Removal is a short in-office procedure. They may use:")

        st.markdown("- Steroid injections to reduce pain or lesion size.")
        st.markdown("- Surgical excision, using a surgical tool to scrape off the lesion.")


